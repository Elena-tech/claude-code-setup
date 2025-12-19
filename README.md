# Claude Code Setup Documentation

A comprehensive guide for setting up Claude Code with MCP (Model Context Protocol) servers, specifically focusing on GitHub integration.

## Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [GitHub MCP Server Setup](#github-mcp-server-setup)
- [Features](#features)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

## About

This repository contains documentation and guides for setting up Claude Code with MCP servers. MCP servers extend Claude Code's capabilities by providing integrations with external services like GitHub, allowing you to interact with repositories, issues, pull requests, and more directly from the command line.

## Prerequisites

- Node.js and npm installed
- Claude Code CLI installed
- GitHub account
- Basic familiarity with command line operations

## Installation

### Installing Claude Code

If you haven't installed Claude Code yet, visit the official documentation for installation instructions.

### Installing GitHub MCP Server

The GitHub MCP server allows Claude Code to interact with GitHub's API for repository management, file operations, and more.

#### Basic Installation

```bash
claude mcp add --scope user github -- npx -y @modelcontextprotocol/server-github
```

#### Installation with GitHub Personal Access Token

For full functionality (creating issues, PRs, pushing code, accessing private repos), you'll need to configure a GitHub Personal Access Token:

```bash
claude mcp add --scope user github -e GITHUB_PERSONAL_ACCESS_TOKEN=your_token_here -- npx -y @modelcontextprotocol/server-github
```

## GitHub MCP Server Setup

### Step 1: Create a GitHub Personal Access Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Claude Code MCP")
4. Select the following scopes:
   - `repo` - Full control of private repositories
   - `workflow` - Update GitHub Action workflows
   - `read:org` - Read org and team membership
   - `user` - Read user profile data
5. Click "Generate token"
6. **Important:** Copy the token immediately (you won't see it again!)

### Step 2: Configure the MCP Server

Run the following command, replacing `YOUR_TOKEN` with your actual GitHub Personal Access Token:

```bash
claude mcp add --scope user github -e GITHUB_PERSONAL_ACCESS_TOKEN=YOUR_TOKEN -- npx -y @modelcontextprotocol/server-github
```

### Step 3: Verify Installation

Check that the server is connected:

```bash
claude mcp list
```

You should see:
```
github: npx -y @modelcontextprotocol/server-github - ✓ Connected
```

View detailed configuration:

```bash
claude mcp get github
```

## Features

With the GitHub MCP server configured, Claude Code can:

### File Operations
- Create and update files in GitHub repositories
- Automatic branch creation for file updates
- Push changes directly to repositories

### Repository Management
- Search for repositories
- Manage branches
- Access both public and private repositories

### Search Capabilities
- Search for issues across repositories
- Search code within repositories
- Find relevant information quickly

### Issue & Pull Request Management
- Create issues programmatically
- Create pull requests from the command line
- Manage GitHub workflows

## Usage Examples

### Example 1: Search for a Repository

Simply ask Claude Code:
```
Search for my repository named "project-name"
```

### Example 2: Create an Issue

```
Create an issue in my repository "repo-name" with title "Bug: Fix login error" and description "Users are unable to login with valid credentials"
```

### Example 3: Create a File in a Repository

```
Create a new file called "CONTRIBUTING.md" in my repository "repo-name" with contribution guidelines
```

### Example 4: Search Code

```
Search for all files containing "API_KEY" in my repository "repo-name"
```

## Troubleshooting

### Server Not Connected

If `claude mcp list` shows the server as disconnected:

1. Check that Node.js and npm are installed: `node --version && npm --version`
2. Try removing and re-adding the server:
   ```bash
   claude mcp remove github -s user
   claude mcp add --scope user github -e GITHUB_PERSONAL_ACCESS_TOKEN=YOUR_TOKEN -- npx -y @modelcontextprotocol/server-github
   ```

### Authentication Issues

If you're getting authentication errors:

1. Verify your token has the correct scopes
2. Check that the token hasn't expired
3. Ensure the token is correctly set in the environment variable

### Permission Errors

If operations fail due to permissions:

1. Ensure your GitHub token has the necessary scopes (`repo`, `workflow`, etc.)
2. Verify you have access to the repository you're trying to modify
3. Check if the repository is private and your token has access to private repos

## Managing MCP Servers

### List All Installed Servers
```bash
claude mcp list
```

### View Server Details
```bash
claude mcp get github
```

### Remove a Server
```bash
claude mcp remove github -s user
```

### Update Server Configuration
```bash
claude mcp update github -e GITHUB_PERSONAL_ACCESS_TOKEN=new_token_here
```

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [GitHub MCP Server on npm](https://www.npmjs.com/package/@modelcontextprotocol/server-github)
- [Model Context Protocol Servers Repository](https://github.com/modelcontextprotocol/servers)
- [Claude Code Documentation](https://claude.ai/code)

## Contributing

Contributions to improve this documentation are welcome! Please feel free to submit issues or pull requests.

## License

This documentation is provided as-is for educational and reference purposes.

---

Generated with [Claude Code](https://claude.ai/code) via [Happy](https://happy.engineering)
