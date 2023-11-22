---
layout: default
lang: en
title: Contributing
---

# Contributing to Black Python Devs

First off, thank you for considering contributing to Black Python Devs website. It's people like you that make Black Python Devs such a great community.

## Code of Conduct

Help us keep this project open and inclusive. Please read and follow our [Code of Conduct](https://github.com/BlackPythonDevs/.github/blob/main/CODE_OF_CONDUCT.md).

## How Can I Contribute?

### 1. Create an Issue (and wait to be assigned)

- Click on the Issues tab in the repository.

  ![Issues tab](/assets/images/issues_tab.png)

- Click on the green button with the label **"New issue"** and you should see the image below:

  ![New issue button](/assets/images/new_issue.png)

- Type in the issue title in the title textbox and type in a clear explanation of the issue in the textarea. You can add images, code snippets, etc to explain your issue.

- Once you are done, you can preview your issue by selecting the Preview tab. If you are satisfied with the issue presentation, you can click on the green "Submit new issue" button to create ypur issue.

- Now you wait for your issue to be assigned to you by a maintainer. You should get an email notification of the issue being assigned to you or you can view the issue assignment in the issue page. It should look similar to this:

  ![Issue assignment](/assets/images/issue_assignment.png)

### 2. Fork the Code

- To fork the repository so you have a copy of the codebase, you will click on the **"Fork"** button from the repository main page

  ![Fork button](/assets/images/fork_button_page.png)

- Clicking on the Fork button takes you to the **"Create New Fork"** page where you select the owner (your personal github account) and click on the Create fork button.

  ![Create new fork page](/assets/images/create_new_fork_page.png)

### 3. Make the changes

- The easiest way to make changes and and test them is by using [![GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/BlackPythonDevs/blackpythondevs.github.io)

- You can also access the Codespaces from the repository main page:

  ![Codespaces tab](/assets/images/codespaces_tab.png)

- The web version of VSCode should open in a new tab in your browser:

  ![BlackPythonDevs Codespace](/assets/images/blackpythondevs_codespace.png)

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

- Submit a Pull Request

🥳

## Accessibility

Accessibility (A11y) using the **FastPass** tests for A11y and the [Accessibility Insights for Web
][1] browser extension.

### 1: Reproduce the Tests

First, reproduce the **FastPass** tests for A11y using the [Accessibility Insights for Web
][1] browser extension. This extension is designed to help you identify and fix accessibility issues on your website.

![image](https://github.com/BlackPythonDevs/blackpythondevs.github.io/assets/44526468/222e6653-c963-4518-a297-262d656216a7)

### 2: Capture the Issues

If the Accessibility Insights for Web extension identifies any issues, capture a screenshot of the issues on the [BPDevs](https://blackpythondevs.github.io/) website. You can do this by pressing <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> on your keyboard.

### 3: Make the Necessary Changes

Next, make the necessary changes to fix the identified issues. This might involve modifying the CSS of the website.

### 4: Test the Changes

After making the changes, run the **FastPass** test again and capture a screenshot showing no accessibility issues. This will serve as proof that the issues have been successfully resolved.

![image](https://github.com/BlackPythonDevs/blackpythondevs.github.io/assets/44526468/9a284f43-3cde-4370-9eab-1d302ed65e9e)

### 5: Check and Pass Other Tests

Finally, check and pass other tests, such as the rules with `pre-commit`. This ensures that your changes are in line with the existing codebase and do not introduce any new issues.

## Translations

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
