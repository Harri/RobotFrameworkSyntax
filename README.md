# Robot Framework syntax for Sublime Text

What's included:

 * Syntax highlighting for Robot Framework
 * Build system for Robot Framework

What's not, and will not be, included:

 * IDE-like features

To get IDE-like features for RF

 1. Install this plugin
 2. Install https://packagecontrol.io/packages/LSP for Sublime Text
 3. execute `pip install robotframework-lsp`
 4. Add 

        "robotframework": {
          "command": ["python", "-m", "robotframework_ls"],
          "enabled": true,
          "languageId": "robotframework",
          "scopes": [
            "source.robot",
            "source.resource"
          ],
          "syntaxes": [
            "Packages/RobotFrameworkSyntax/Robot Framework.sublime-syntax"
          ]
        }
  
  to LSP settings' clients.

## How to install

Download this repository as zip or git clone, then in Sublime Text navigate to *Preferences* > *Browser Packages...*. Create new directory *RobotFrameworkSyntax* and copy all files from the zip/git repository to there.

## Obligatory example image

![Screenshot showing Robot Framework Syntax in action](sublimerobot.png "Screenshot showing Robot Framework Syntax in action")
