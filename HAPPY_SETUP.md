# Happy App - Complete Setup Guide

Happy is a free, open-source mobile and web client for Claude Code that enables you to control Claude AI from your phone with end-to-end encryption and seamless workflow continuity.

## Table of Contents

- [What is Happy?](#what-is-happy)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Initial Configuration](#initial-configuration)
- [Connecting to Claude Account](#connecting-to-claude-account)
- [Running Commands](#running-commands)
- [Features](#features)
- [Troubleshooting](#troubleshooting)
- [Advanced Configuration](#advanced-configuration)
- [Resources](#resources)

## What is Happy?

Happy is a mobile and web client for Claude Code that lets you:

- **Control Claude Code from your phone** - Continue conversations seamlessly between desktop and mobile
- **Use voice coding** - Speak to Claude instead of typing
- **Get push notifications** - Receive alerts for permission requests and task completion
- **Work securely** - End-to-end encryption using the same technology as Signal (TweetNaCl)
- **Stay synchronized** - Access conversation history even when your terminal is offline
- **Run multiple sessions** - Spawn and control multiple Claude Code instances in parallel

### How It Works

Happy consists of three components:

1. **CLI Program (`happy`)** - Runs on your computer, starts Claude Code sessions, and encrypts all communication
2. **Relay Server** - Passes encrypted messages between your computer and phone (cannot read your data)
3. **Mobile/Web App** - Provides a native mobile experience for Claude Code

## Prerequisites

Before installing Happy, ensure you have:

- **Node.js 18 or later** (released April 19, 2022)
  ```bash
  node --version  # Should show v18.0.0 or higher
  ```

- **Claude CLI installed and authenticated**
  ```bash
  claude --version  # Should show Claude CLI version
  ```
  If not installed, follow the [official Claude Code installation guide](https://claude.ai/code)

- **A smartphone** (iOS, Android) or web browser for the mobile client

## Installation

### Step 1: Install Happy CLI

Install the Happy CLI globally using npm:

```bash
npm install -g happy-coder
```

### Step 2: Verify Installation

Check that Happy was installed correctly:

```bash
happy --version
```

You should see the version number displayed.

### Step 3: Install Happy Mobile App

Choose your platform:

- **iOS**: Download from the [App Store](https://apps.apple.com/us/app/happy-claude-code-client/id6748571505)
- **Android**: Download from Google Play Store
- **Web**: Visit [happy.engineering](https://happy.engineering)

## Initial Configuration

### Configure Happy CLI

The Happy CLI works with your existing Claude Code configuration. No additional configuration files are needed for basic usage.

### First-Time Setup

1. **Ensure Claude CLI is authenticated**:
   ```bash
   claude auth status
   ```

   If not authenticated, run:
   ```bash
   claude auth login
   ```

2. **Test Claude Code**:
   ```bash
   claude
   ```

   This should start a normal Claude Code session. Type `exit` to quit.

## Connecting to Claude Account

Happy uses your existing Claude authentication. The connection process links your mobile device to your computer's Claude Code sessions.

### Step 1: Start Happy with Authentication

Run the authentication command to generate a QR code:

```bash
happy --auth
```

This will:
- Start the Happy CLI
- Generate a unique QR code in your terminal
- Display pairing instructions

### Step 2: Scan QR Code from Mobile App

1. Open the **Happy app** on your phone
2. Tap the **"Pair Device"** or **"Add Device"** button
3. Point your camera at the QR code displayed in your terminal
4. Wait for the confirmation message

### Step 3: Verify Connection

Once paired, you should see:
- ✅ "Device paired successfully" message in your terminal
- ✅ Your computer appearing in the Happy app's device list
- ✅ Green connection status indicator

### Security Note

The pairing process establishes end-to-end encryption between your devices using TweetNaCl (the same encryption library used by Signal). The relay server cannot decrypt your messages or code.

## Running Commands

### Basic Usage

Once paired, you can use Happy in several ways:

#### 1. Start a New Happy Session (Desktop)

```bash
happy
```

This starts a Claude Code session that's synchronized with your mobile device. You can now:
- Continue the conversation from your phone
- Receive push notifications
- Switch between devices seamlessly

#### 2. Use Happy from Mobile

- Open the Happy app on your phone
- Tap **"New Conversation"**
- Start talking to Claude (text or voice)
- Your desktop terminal will show the conversation in real-time

#### 3. Continue Existing Conversations

- **On Desktop**: Run `happy` to see recent conversations
- **On Mobile**: Open the Happy app to see conversation history
- Tap any conversation to continue where you left off

### Command Examples

#### Start a Coding Session
```bash
happy
```
Then ask Claude: "Help me set up a new React project"

#### Use Voice Coding (Mobile Only)
1. Open Happy app
2. Tap the microphone icon
3. Speak your request: "Create a new Python function to calculate fibonacci numbers"
4. Happy will transcribe and send to Claude

#### Run Multiple Claude Code Instances

Terminal 1:
```bash
happy
# Ask Claude to work on Feature A
```

Terminal 2:
```bash
happy
# Ask Claude to work on Feature B
```

Both sessions are accessible from your mobile device.

### Advanced Command Options

```bash
# Start Happy with specific configuration
happy --config /path/to/config.json

# Start Happy in verbose mode for debugging
happy --verbose

# Show authentication QR code
happy --auth

# Display help
happy --help
```

## Features

### Push Notifications

Receive mobile notifications for:
- **Permission requests** - When Claude needs approval for file operations
- **Task completion** - When long-running tasks finish
- **Errors** - When something goes wrong

Configure notification settings in the Happy mobile app.

### Voice Coding

Use your voice to code:
1. Tap the microphone icon in the Happy app
2. Speak naturally: "Create a function that validates email addresses"
3. Happy transcribes and sends to Claude
4. Claude responds with code and explanations

### Conversation History

- Access full conversation history from mobile, even when your terminal is offline
- Search through past conversations
- Resume any previous session
- Sync across all paired devices

### File Management

- View file mentions and edits in mobile interface
- Approve file operations from your phone
- See diffs and changes in a mobile-friendly format

### Slash Commands

Use all Claude Code slash commands from mobile:
- `/help` - Get help
- `/clear` - Clear conversation
- `/reset` - Reset session
- Custom slash commands work too

## Troubleshooting

### Happy Command Not Found

**Problem**: `happy: command not found`

**Solutions**:
1. Ensure npm global bin is in your PATH:
   ```bash
   npm config get prefix
   ```
   Add `<prefix>/bin` to your PATH

2. Reinstall Happy CLI:
   ```bash
   npm install -g happy-coder
   ```

### QR Code Won't Scan

**Problem**: Mobile app can't scan the QR code

**Solutions**:
1. Make your terminal window larger (QR code may be too small)
2. Increase terminal font size
3. Try better lighting conditions
4. Ensure camera permissions are enabled in the Happy app
5. Try manually entering the pairing code displayed below the QR code

### Connection Drops Frequently

**Problem**: Mobile app disconnects from desktop

**Solutions**:
1. Check your internet connection on both devices
2. Ensure your firewall isn't blocking Happy
3. Try restarting the Happy CLI:
   ```bash
   # Press Ctrl+C to stop
   happy  # Start again
   ```
4. Re-pair your devices using `happy --auth`

### Claude CLI Not Authenticated

**Problem**: `Error: Claude CLI not authenticated`

**Solutions**:
1. Authenticate Claude CLI:
   ```bash
   claude auth login
   ```
2. Verify authentication:
   ```bash
   claude auth status
   ```

### Node.js Version Too Old

**Problem**: `Error: Node.js version 18 or higher required`

**Solutions**:
1. Update Node.js:
   ```bash
   # Using nvm (recommended)
   nvm install 18
   nvm use 18

   # Or download from nodejs.org
   ```
2. Verify version:
   ```bash
   node --version
   ```

### Messages Not Syncing

**Problem**: Changes in terminal don't appear on mobile (or vice versa)

**Solutions**:
1. Check connection status in Happy app (should show green)
2. Restart the Happy CLI session
3. Check if relay server is accessible:
   ```bash
   happy --verbose  # Shows connection details
   ```
4. Ensure both devices have internet connectivity

### Push Notifications Not Working

**Problem**: Not receiving notifications on mobile

**Solutions**:
1. Check notification permissions in phone settings
2. Enable notifications in Happy app settings
3. Ensure the app isn't being killed by battery optimization:
   - iOS: Settings → Happy → Background App Refresh → On
   - Android: Settings → Apps → Happy → Battery → Unrestricted

## Advanced Configuration

### Custom Relay Server

If you want to run your own relay server for additional privacy:

1. Clone the Happy server repository:
   ```bash
   git clone https://github.com/slopus/happy
   ```

2. Follow the server setup instructions in the repository

3. Configure Happy CLI to use your server:
   ```bash
   happy --server https://your-server.com
   ```

### Configuration File

Create a configuration file at `~/.happy/config.json`:

```json
{
  "server": "https://relay.happy.engineering",
  "encryption": "tweetnacl",
  "notifications": {
    "enabled": true,
    "permissions": true,
    "completion": true,
    "errors": true
  },
  "voice": {
    "enabled": true,
    "language": "en-US"
  }
}
```

### Environment Variables

Control Happy behavior with environment variables:

```bash
# Custom relay server
export HAPPY_SERVER="https://your-server.com"

# Enable debug logging
export HAPPY_DEBUG=true

# Custom config path
export HAPPY_CONFIG="~/my-happy-config.json"
```

### Multiple Device Pairing

You can pair multiple devices to the same computer:

1. Run `happy --auth` on your computer
2. Scan with first device
3. Run `happy --auth` again
4. Scan with second device

All devices will be synchronized and receive the same conversations.

### Unpairing Devices

To unpair a device:

1. Open Happy app on mobile
2. Go to Settings → Devices
3. Find the device to remove
4. Tap "Unpair" or "Remove"

Or from CLI:
```bash
happy --unpair-all  # Remove all paired devices
```

## Integration with Claude Code Features

### Using with MCP Servers

Happy works seamlessly with MCP servers (like the GitHub MCP server):

```bash
# Configure GitHub MCP server (if not already done)
claude mcp add github --scope user

# Start Happy session
happy

# Now you can use GitHub operations from mobile:
# "Search my repositories for project-name"
# "Create an issue in my repo about the login bug"
```

### File Operations from Mobile

When Claude requests file operations:
1. You'll receive a push notification on your phone
2. Open Happy app to review the operation
3. Approve or deny from mobile
4. Claude continues working based on your response

### Using Custom Agents

If you've configured custom agents in Claude Code, they're available through Happy:

```bash
happy
# Then use your custom agents as normal
```

## Tips and Best Practices

### 1. Keep Happy CLI Running
For the best experience, keep the `happy` command running in a terminal tab or use a terminal multiplexer like `tmux`:

```bash
# Start tmux session
tmux new -s happy

# Inside tmux, run happy
happy

# Detach with Ctrl+B, then D
# Reattach later with: tmux attach -t happy
```

### 2. Use Voice for Quick Queries
Voice coding is great for:
- Quick questions while away from keyboard
- Reviewing code during meetings
- Getting quick explanations
- Starting new tasks

### 3. Organize with Multiple Sessions
Use different Happy sessions for different projects:
- One session for frontend work
- Another for backend
- Another for documentation

### 4. Enable All Notifications
Enable all notification types to stay informed:
- Permission requests (critical)
- Task completion (helpful for long operations)
- Errors (important for debugging)

## Resources

### Official Documentation
- [Happy Engineering Homepage](https://happy.engineering/)
- [Quick Start Guide](https://happy.engineering/docs/quick-start/)
- [All Features Documentation](https://happy.engineering/docs/features/)

### GitHub Repositories
- [Happy Mobile/Web Client](https://github.com/slopus/happy)
- [Happy CLI](https://github.com/slopus/happy-cli)

### App Downloads
- [iOS App Store](https://apps.apple.com/us/app/happy-claude-code-client/id6748571505)
- [Android Google Play](https://play.google.com/store/apps/details?id=engineering.happy.app)

### Tutorials and Guides
- [The Definitive Guide to Using Claude Code on Your Phone](https://sealos.io/blog/claude-code-on-phone)
- [3 Ways to Use Claude Code on Mobile](https://apidog.com/blog/claude-code-mobile/)

### Support
- GitHub Issues: Report bugs or request features in the respective repositories
- Community: Join discussions on the Happy GitHub repositories

## FAQ

**Q: Is Happy free?**
A: Yes, Happy is completely free and open-source.

**Q: Is my code secure?**
A: Yes, Happy uses end-to-end encryption (TweetNaCl, same as Signal). The relay server cannot decrypt your messages.

**Q: Can I use Happy without mobile?**
A: Yes, `happy` works as a regular Claude Code session even without mobile pairing.

**Q: Does Happy work with Claude Desktop?**
A: No, Happy is specifically for Claude Code (CLI). For desktop, use the official Claude app.

**Q: Can I use Happy offline?**
A: You need internet for initial connection, but conversation history is cached and viewable offline on mobile.

**Q: What's the difference between `claude` and `happy` commands?**
A: `happy` wraps `claude` and adds mobile sync, encryption, and push notifications. All Claude Code features work in Happy.

**Q: Can multiple people pair to the same Happy session?**
A: No, Happy sessions are personal. Each user should run their own `happy` instance.

---

Generated with [Claude Code](https://claude.ai/code) via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
