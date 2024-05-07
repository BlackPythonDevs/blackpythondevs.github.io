---
layout: default
lang: en
title: Contributing
---

# Contributing at Black Python Devs

First off, thank you for considering contributing to Black Python Devs website. It's people like you that make Black Python Devs such a great community. Navigate through the following to understand more about contributing here.

- [Before You Get Started](#before-you-get-started)
- [How to Contribute](#how-to-contribute)
- [Accessibility](#accessibility)
- [Translations](#translations)

# Before You Get Started

## Code of Conduct

Black Python Devs follows the following [Code of Conduct](https://github.com/BlackPythonDevs/.github/blob/main/CODE_OF_CONDUCT.md) . The comfort and safety of Black Python Devs community members are our priority. Please do well to adhere to the Code of Conduct to participate in the Black Python Devs community.

## Issues & Pull Requests

### Creating an issue

Before **creating** an issue i.e for `features`/`bugs`/`improvements` please follow these steps:

1. Search existing issues before creating a new issue (look to see if the issue has already been created).
1. If it doesn't exist create a new issue giving as much context as possible (please take note and select the correct issue type, for example `bug`, `documentation` or `feature`.
1. If you wish to work on the issue add this to the issue description.

### Working on an issue

Before working on an existing issue please follow these steps:

1. Comment asking for the issue to be assigned to you.
1. To best position yourself for issues assignment, we recommend that you:
   1. Confirm that you have read the CONTRIBUTING.md.
   1. Have a functional development environment (have built and are able to run the project).
   1. Convey your intended approach to solving the issue.
   1. Put each of these items in writing in one or more comments.
1. After the issue is assigned to you, you can start working on it.
1. In general, **only** start working on this issue (and open a Pull Request) when it has been assigned to you. Doing so will prevent confusion, duplicate work (some of which may go unaccepted given its duplicity), incidental stepping on toes, and the headache involved for maintainers and contributors alike as issue assignments collide and heads bump together.
1. Reference the issue in your Pull Request (for example `This PR fixes #123`), so that the corresponding issue is automatically closed upon merge of your Pull Request.

> Notes:
>
> - Check the `Assignees` box at the top of the page to see if the issue has been assigned to someone else before requesting this be assigned to you. If the issue has a current Assignee, but appears to be inactive, politely inquire with the current Assignee as to whether they are still working on a solution and/or if you might collaborate with them.
> - Only request to be assigned an issue if you know how to work on it.
> - If an issue is unclear, ask questions to get more clarity before asking to have the issue assigned to you; avoid asking "what do I do next? how do I fix this?" (see the item above this line)
> - An issue can be assigned to multiple people, if you all agree to collaborate on the issue (the Pull Request can contain commits from different collaborators)
> - Any issues that has no activity after 2 weeks will be unassigned and re-assigned to someone else.

## Reviewing Pull Requests

We welcome everyone to review Pull Requests. It is a great way to learn, network, and support each other.

### DOs

- Use inline comments to explain your suggestions
- Use inline suggestions to propose changes
- Exercise patience and empathy while offering critiques of the works of others.

### DON'Ts

- Do not repeat feedback, this creates more noise than value (check the existing conversation), use GitHub reactions if you agree/disagree with a comment
- Do not blindly approve Pull Requests to improve your GitHub contributors graph

## Discord Community

Join the [Discord](https://discord.gg/XUc3tFqCT3) to discuss suggested new features, possible bugs, enhancement in user experience, and any other aspects of the site. The comment section of each issue is our preferred method of communication as it retains conversations history for future contributors wanting to gain insights/updates on the topic in question, you can, however, inquire in the #community-discussion channel in the Black Python Devs Discord workspace.

# Contributing to Black Python Devs Projects

Please follow these steps and note these guidelines to begin contributing:

1. First step is to set up the local development environment.
1. Bug fixes are always welcome. Start by reviewing the [list of bugs](https://github.com/BlackPythonDevs/blackpythondevs.github.io/issues).
1. A good way to easily start contributing is to pick and work on a [good first issue](https://github.com/BlackPythonDevs/blackpythondevs.github.io/labels/good%20first%20issue). We try to make these issues as clear as possible and provide basic info on how the code should be changed, and if something is unclear feel free to ask for more information on the issue.

# How to Contribute

## Fork the repository

- To fork the repository so you have a copy of the codebase, you will click on the **"Fork"** button from the repository main page

  ![Fork button](/assets/images/fork_button_page.png)

- Clicking on the Fork button takes you to the **"Create New Fork"** page where you select the owner (your personal github account) and click on the Create fork button.

  ![Create new fork page](/assets/images/create_new_fork_page.png)

## Createing an issue

- Click on the issues tab in the repository.

  ![issues tab](/assets/images/issues_tab.png)

- Click on the green button with the label **"New issue"** and you should see the image below:

  ![New issue button](/assets/images/new_issue.png)

- Type in the issue title in the title textbox and type in a clear explanation of the issue in the textarea. You can add images, code snippets, etc to explain your issue.

- Once you are done, you can preview your issue by selecting the Preview tab. If you are satisfied with the issue presentation, you can click on the green "Submit new issue" button to create your issue.

- And that's it! If you cose to comment requesting the issue to be assigned to you, wait for a maintainer to do so. You should get an email notification of the issue being assigned to you or you can view the issue assignment in the issue page. It should look similar to this:

  ![issue assignment](/assets/images/issue_assignment.png)

## Working on an issue

- The easiest way to make changes and and test them is by using [![GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/BlackPythonDevs/blackpythondevs.github.io)

- You can also access the Codespaces from the repository main page:

  ![Codespaces tab](/assets/images/codespaces_tab.png)

- The web version of VSCode should open in a new tab in your browser:

  ![Black Python Devs Codespace](/assets/images/BlackPythonDevs_codespace.png)

- Now that you have the code editor set up, you need to install the dependencies. To do this, you have to open the code editor's terminal and run the command `bundle install`.

- The easiest way to open the terminal is to click on the 3 horizontal lines (also known as hamburger) at the top left of the code editor > Terminal > New Terminal:

  ![Terminal starter](/assets/images/terminal_starter3.png)

- In the terminal run the command `bundle install`.

  ![Bundle install terminal](/assets/images/bundle_install_terminal.png)

- After installing the dependencies, its time to run the application. We do this by running the command `bundle exec jekyll serve` or run the default **Build Task** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>:

  ![Jekyll serve terminal](/assets/images/jekyll_serve_terminal.png)

- The server address shows `http://127.0.0.1:4000`. This is the address for any local computer so this server will be wrong since the application is running on a remote computer so we have to get the address of that computer. We can get the address by clicking on the Ports tab next to the Terminal:

  ![Codespace ports](/assets/images/codespace_ports2.png)

- <kbd>Ctrl</kbd> + Click on the Forwarded Address assigned to Port 4000. This will open the running application in a new tab:

  ![Running page](/assets/images/running_page.png)

- Test your changes (create new tests as needed)

- Once you’ve committed and pushed all of your changes to GitHub, go to the page for your fork on GitHub, select your development branch, and click the pull request button. Please ensure that you compare your feature branch to the desired branch of the repo you are supposed to make a PR to. If you need to make any adjustments to your pull request, just push the updates to GitHub. Your pull request will automatically track the changes in your development branch and update it. 🥳

# Accessibility

Accessibility (A11y) using the **FastPass** tests for A11y and the [Accessibility Insights for Web
][1] browser extension.

## 1: Reproduce the Tests

First, reproduce the **FastPass** tests for A11y using the [Accessibility Insights for Web
][1] browser extension. This extension is designed to help you identify and fix accessibility issues on your website.

![image](https://github.com/BlackPythonDevs/blackpythondevs.github.io/assets/44526468/222e6653-c963-4518-a297-262d656216a7)

## 2: Capture the issues

If the Accessibility Insights for Web extension identifies any issues, capture a screenshot of the issues on the [BPDevs](https://BlackPythonDevs.github.io/) website. You can do this by pressing <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> on your keyboard.

## 3: Make the Necessary Changes

Next, make the necessary changes to fix the identified issues. This might involve modifying the CSS of the website.

## 4: Test the Changes

After making the changes, run the **FastPass** test again and capture a screenshot showing no accessibility issues. This will serve as proof that the issues have been successfully resolved.

![image](https://github.com/BlackPythonDevs/blackpythondevs.github.io/assets/44526468/9a284f43-3cde-4370-9eab-1d302ed65e9e)

## 5: Check and Pass Other Tests

Finally, check and pass other tests, such as the rules with `pre-commit`. This ensures that your changes are in line with the existing codebase and do not introduce any new issues.

# Translations

We welcome translations for the Black Python Devs website in all languages! Here's how you can contribute:

The language code being used should be in the format [<ISO 639-1>](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

1. [**Fork the repository**](#2-fork-the-code): Make a copy of this project on your account.

2. **Create a new branch**: Make a new branch for your translation work to keep it separate from the main project: e.g. `es` .

3. **Translate**: Translate all the content in your preferred language. Please ensure that the translation is accurate and professional.

   - Copy `_data/locales/en.yml` to your target language file e.g. `_data/locales/es.yml` and translate all the strings.

   - Create a new directory in `_articles/` for your language e.g. `_articles/es/`, copy each guide from `_articles/` into that folder and translate the content in each guide.

   - Copy `index.html` to your target language index file e.g. [`_articles/es/index.html`](https://github.com/BlackPythonDevs/blackpythondevs.github.io/blob/HEAD/_articles/es/index.html) and update the `lang:` and add the `permalink:` fields. Example: `lang: es` and `permalink: /es/`.

4. **Submit a Pull Request**: You may send a pull request before all steps above are complete: e.g., you may want to ask for help with translations, or getting tests to pass. However, your pull request will not be merged until all steps above are complete.

Our maintainers will review your pull request and merge it if everything is in order. We appreciate your contribution to making Black Python Devs accessible to more people around the world!

[1]: https://microsoftedge.microsoft.com/addons/detail/accessibility-insights-fo/ghbhpcookfemncgoinjblecnilppimih
