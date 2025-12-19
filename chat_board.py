#!/usr/bin/env python3
"""
Conversational Chat Board - A simple terminal-based chat application
Allows users to create conversations, post messages, view message history, and more.
"""

import json
import os
import datetime
from typing import List, Dict, Optional


class Message:
    """Represents a single message in a conversation"""

    def __init__(self, author: str, content: str, timestamp: Optional[str] = None):
        self.author = author
        self.content = content
        self.timestamp = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        """Convert message to dictionary for JSON serialization"""
        return {
            "author": self.author,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Message':
        """Create message from dictionary"""
        return cls(data["author"], data["content"], data["timestamp"])

    def __str__(self) -> str:
        """String representation of the message"""
        return f"[{self.timestamp}] {self.author}: {self.content}"


class Conversation:
    """Represents a conversation thread with multiple messages"""

    def __init__(self, title: str, conversation_id: Optional[int] = None):
        self.title = title
        self.conversation_id = conversation_id
        self.messages: List[Message] = []
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_message(self, message: Message):
        """Add a message to the conversation"""
        self.messages.append(message)

    def get_message_count(self) -> int:
        """Get the total number of messages in this conversation"""
        return len(self.messages)

    def to_dict(self) -> Dict:
        """Convert conversation to dictionary for JSON serialization"""
        return {
            "title": self.title,
            "conversation_id": self.conversation_id,
            "created_at": self.created_at,
            "messages": [msg.to_dict() for msg in self.messages]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Conversation':
        """Create conversation from dictionary"""
        conv = cls(data["title"], data["conversation_id"])
        conv.created_at = data["created_at"]
        conv.messages = [Message.from_dict(msg) for msg in data["messages"]]
        return conv


class ChatBoard:
    """Main chat board application managing multiple conversations"""

    def __init__(self, storage_file: str = "chat_board_data.json"):
        self.storage_file = storage_file
        self.conversations: List[Conversation] = []
        self.current_user: Optional[str] = None
        self.next_conversation_id = 1
        self.load_data()

    def load_data(self):
        """Load conversations from storage file"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.conversations = [Conversation.from_dict(conv) for conv in data.get("conversations", [])]
                    self.next_conversation_id = data.get("next_conversation_id", 1)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Warning: Could not load data file: {e}")
                self.conversations = []

    def save_data(self):
        """Save conversations to storage file"""
        data = {
            "conversations": [conv.to_dict() for conv in self.conversations],
            "next_conversation_id": self.next_conversation_id
        }
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=2)

    def set_username(self, username: str):
        """Set the current user's name"""
        self.current_user = username

    def create_conversation(self, title: str) -> Conversation:
        """Create a new conversation"""
        conversation = Conversation(title, self.next_conversation_id)
        self.next_conversation_id += 1
        self.conversations.append(conversation)
        self.save_data()
        return conversation

    def get_conversation(self, conversation_id: int) -> Optional[Conversation]:
        """Get a conversation by ID"""
        for conv in self.conversations:
            if conv.conversation_id == conversation_id:
                return conv
        return None

    def list_conversations(self) -> List[Conversation]:
        """Get all conversations"""
        return self.conversations

    def delete_conversation(self, conversation_id: int) -> bool:
        """Delete a conversation by ID"""
        for i, conv in enumerate(self.conversations):
            if conv.conversation_id == conversation_id:
                self.conversations.pop(i)
                self.save_data()
                return True
        return False

    def post_message(self, conversation_id: int, content: str) -> bool:
        """Post a message to a conversation"""
        conversation = self.get_conversation(conversation_id)
        if conversation and self.current_user:
            message = Message(self.current_user, content)
            conversation.add_message(message)
            self.save_data()
            return True
        return False


class ChatBoardUI:
    """Terminal-based user interface for the chat board"""

    def __init__(self):
        self.chat_board = ChatBoard()
        self.running = True

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title: str):
        """Print a formatted header"""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)

    def print_separator(self):
        """Print a separator line"""
        print("-" * 60)

    def get_input(self, prompt: str) -> str:
        """Get user input with a prompt"""
        return input(f"\n{prompt}: ").strip()

    def display_main_menu(self):
        """Display the main menu"""
        self.print_header("CONVERSATIONAL CHAT BOARD")
        print("\nMain Menu:")
        print("  1. List all conversations")
        print("  2. Create new conversation")
        print("  3. Open conversation")
        print("  4. Delete conversation")
        print("  5. Change username")
        print("  6. Exit")
        self.print_separator()

    def list_conversations_ui(self):
        """Display all conversations"""
        self.clear_screen()
        self.print_header("ALL CONVERSATIONS")

        conversations = self.chat_board.list_conversations()

        if not conversations:
            print("\nNo conversations yet. Create one to get started!")
        else:
            for conv in conversations:
                msg_count = conv.get_message_count()
                print(f"\n  ID: {conv.conversation_id}")
                print(f"  Title: {conv.title}")
                print(f"  Created: {conv.created_at}")
                print(f"  Messages: {msg_count}")
                self.print_separator()

        input("\nPress Enter to continue...")

    def create_conversation_ui(self):
        """Create a new conversation"""
        self.clear_screen()
        self.print_header("CREATE NEW CONVERSATION")

        title = self.get_input("Enter conversation title")

        if title:
            conversation = self.chat_board.create_conversation(title)
            print(f"\n✓ Conversation '{title}' created successfully!")
            print(f"  Conversation ID: {conversation.conversation_id}")
        else:
            print("\n✗ Title cannot be empty!")

        input("\nPress Enter to continue...")

    def open_conversation_ui(self):
        """Open and interact with a conversation"""
        self.clear_screen()
        self.print_header("OPEN CONVERSATION")

        conversations = self.chat_board.list_conversations()

        if not conversations:
            print("\nNo conversations available. Create one first!")
            input("\nPress Enter to continue...")
            return

        # List available conversations
        print("\nAvailable conversations:")
        for conv in conversations:
            print(f"  {conv.conversation_id}. {conv.title} ({conv.get_message_count()} messages)")

        try:
            conv_id = int(self.get_input("\nEnter conversation ID"))
            conversation = self.chat_board.get_conversation(conv_id)

            if conversation:
                self.conversation_menu(conversation)
            else:
                print("\n✗ Conversation not found!")
                input("\nPress Enter to continue...")
        except ValueError:
            print("\n✗ Invalid conversation ID!")
            input("\nPress Enter to continue...")

    def conversation_menu(self, conversation: Conversation):
        """Display conversation menu and handle interactions"""
        while True:
            self.clear_screen()
            self.print_header(f"CONVERSATION: {conversation.title}")

            # Display messages
            if conversation.messages:
                print("\nMessage History:")
                self.print_separator()
                for msg in conversation.messages:
                    print(f"\n{msg}")
                self.print_separator()
            else:
                print("\nNo messages yet. Be the first to post!")

            # Display menu
            print("\nOptions:")
            print("  1. Post a message")
            print("  2. Refresh messages")
            print("  3. Back to main menu")

            choice = self.get_input("\nEnter your choice (1-3)")

            if choice == "1":
                self.post_message_ui(conversation)
            elif choice == "2":
                # Reload conversation to get latest messages
                updated_conv = self.chat_board.get_conversation(conversation.conversation_id)
                if updated_conv:
                    conversation = updated_conv
            elif choice == "3":
                break
            else:
                print("\n✗ Invalid choice!")
                input("\nPress Enter to continue...")

    def post_message_ui(self, conversation: Conversation):
        """Post a message to a conversation"""
        print("\n" + "=" * 60)
        print("POST MESSAGE")
        print("=" * 60)

        if not self.chat_board.current_user:
            print("\n✗ You must set a username first!")
            input("\nPress Enter to continue...")
            return

        content = self.get_input("Enter your message (or press Enter to cancel)")

        if content:
            success = self.chat_board.post_message(conversation.conversation_id, content)
            if success:
                print(f"\n✓ Message posted successfully!")
                # Reload conversation to show new message
                updated_conv = self.chat_board.get_conversation(conversation.conversation_id)
                if updated_conv:
                    conversation.messages = updated_conv.messages
            else:
                print("\n✗ Failed to post message!")

        input("\nPress Enter to continue...")

    def delete_conversation_ui(self):
        """Delete a conversation"""
        self.clear_screen()
        self.print_header("DELETE CONVERSATION")

        conversations = self.chat_board.list_conversations()

        if not conversations:
            print("\nNo conversations to delete!")
            input("\nPress Enter to continue...")
            return

        # List available conversations
        print("\nAvailable conversations:")
        for conv in conversations:
            print(f"  {conv.conversation_id}. {conv.title}")

        try:
            conv_id = int(self.get_input("\nEnter conversation ID to delete"))

            confirm = self.get_input(f"Are you sure you want to delete conversation {conv_id}? (yes/no)")

            if confirm.lower() in ['yes', 'y']:
                success = self.chat_board.delete_conversation(conv_id)
                if success:
                    print(f"\n✓ Conversation {conv_id} deleted successfully!")
                else:
                    print(f"\n✗ Conversation {conv_id} not found!")
            else:
                print("\n✗ Deletion cancelled!")
        except ValueError:
            print("\n✗ Invalid conversation ID!")

        input("\nPress Enter to continue...")

    def change_username_ui(self):
        """Change the current username"""
        self.clear_screen()
        self.print_header("CHANGE USERNAME")

        current = self.chat_board.current_user or "Not set"
        print(f"\nCurrent username: {current}")

        username = self.get_input("Enter new username")

        if username:
            self.chat_board.set_username(username)
            print(f"\n✓ Username changed to: {username}")
        else:
            print("\n✗ Username cannot be empty!")

        input("\nPress Enter to continue...")

    def run(self):
        """Main application loop"""
        # Welcome screen
        self.clear_screen()
        self.print_header("WELCOME TO CONVERSATIONAL CHAT BOARD")
        print("\nA simple terminal-based chat application")
        print("Create conversations, post messages, and more!")

        # Set initial username
        username = self.get_input("\nEnter your username")
        if username:
            self.chat_board.set_username(username)
            print(f"\nWelcome, {username}!")
        else:
            print("\nNo username set. You can set it later from the menu.")

        input("\nPress Enter to continue...")

        # Main menu loop
        while self.running:
            self.clear_screen()
            self.display_main_menu()

            if self.chat_board.current_user:
                print(f"\nLogged in as: {self.chat_board.current_user}")
            else:
                print("\nWarning: No username set! Set one to post messages.")

            choice = self.get_input("\nEnter your choice (1-6)")

            if choice == "1":
                self.list_conversations_ui()
            elif choice == "2":
                self.create_conversation_ui()
            elif choice == "3":
                self.open_conversation_ui()
            elif choice == "4":
                self.delete_conversation_ui()
            elif choice == "5":
                self.change_username_ui()
            elif choice == "6":
                self.clear_screen()
                print("\nThank you for using Conversational Chat Board!")
                print("Goodbye!\n")
                self.running = False
            else:
                print("\n✗ Invalid choice! Please enter a number from 1-6.")
                input("\nPress Enter to continue...")


def main():
    """Application entry point"""
    try:
        app = ChatBoardUI()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
        print("Please report this issue if it persists.\n")


if __name__ == "__main__":
    main()
