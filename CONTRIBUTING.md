# Contributing to Black Python Devs Projects

Follow these steps and note these guidelines to begin contributing:

1. First step is to set up the local development environment.
2. Bug fixes are always welcome. Start by reviewing the [list of bugs](https://github.com/BlackPythonDevs/blackpythondevs.github.io/issues).
3. A good way to easily start contributing is to pick and work on a [good first issue](https://github.com/BlackPythonDevs/blackpythondevs.github.io/labels/good%20first%20issue). We try to make these issues as clear as possible and provide basic info on how the code should be changed, and if something is unclear feel free to ask for more information on the issue.

# Diagram of the infrastructure in use

Below are some diagrams to best explain the file structure of the website, the development structure and how some information are been generated

## Website structure

The diagram below illustrates the main navigation structure of BPD website, showing how the homepage `(Index)` connects to various sections, including the `Home`, `Blog`, `About Us`, `Events`, and `Community`. Each blog article, represented as `Article1` and `Article2`, is linked directly from the `Blog` section.

```
Website Structure:
Index/
├── Home
├── Blog/
│   ├── Article1
│   └── Article2
├── About Us
├── Events
├── Sponsored Events
├── Community
└── Sponsor Us
```


## Development structure

The diagram below outlines the file structure of the development environment. The root node represents the main directory, containing essential files and folders like `_config.yml`, `_posts`, `_layouts`, `_includes`, `_data`, `_articles`, and `assets`. Each folder contains further organization of specific files. This will aid contributors in understanding how the project is organized and where different components are located.

```
Development Structure:
root/
├── _archive # old pages that should mostly be ignored
├── _posts/
│   ├── post1
│   └── post2
├── _layouts/
│   └── _includes/
├── _data/ # This is where yaml and json files live
│   ├── data_file1
│   └── data_file2
├── assets/ # static files that will be copied over
│   ├── css/
│   ├── images/
│   └── js/
├── pages/ # static pages represented in Render Engine und
├── about.md # content pages
├── index.html
└── tests/
```

## How Pages are generated

The website uses render engine to read `app.py`. You can learn more about Render Engine on their [docs page](https://render-engine.readthedocs.io/en/stable/). The important locations to know.

`app.py` is the instruction file for render engine.

The diagram below explains how information is generated for the about page, showing how the `about.md`(source content) connects with other contents, templates and configuration files. The `about.md` file links to `_layouts/default.html` and `_includes/header.html` and `footer.html`, which define the page layout and thus generates a `about.html` this html file can be styled and scripted with files in the `assets/` folder. This diagram clarifies the rendering process and how different files work together to create the final output for the about page.

```python
@app.page
class About(Page):
    template = "about.html"
    data = yaml.safe_load(pathlib.Path("_data/leadership.yaml").read_text())
```

```

```

The `@app.page` tells Render Engine that we're build a single page vs a collection of pages.

The `class About(Page):` tells us about the Page object. Attributes will pass information on render engine and the jinja template that will be loaded

# How to Contribute

## Fork the repository

- To fork the repository so you have a copy of the codebase, you will click on the **"Fork"** button from the repository main page

  ![Fork button](/assets/images/fork_button_page.png)

- Clicking on the Fork button takes you to the **"Create New Fork"** page where you select the owner (your personal github account) and click on the Create fork button.

  ![Create new fork page](/assets/images/create_new_fork_page.png)

## Creating an issue

- Click on the issues tab in the repository.

  ![issues tab](/assets/images/issues_tab.png)

- Click on the green button with the label **"New issue"** and you should see the image below:

  ![New issue button](/assets/images/new_issue.png)

- Type in the issue title in the title textbox and type in a clear explanation of the issue in the textarea. You can add images, code snippets, etc to explain your issue.

- Once you are done, you can preview your issue by selecting the Preview tab. If you are satisfied with the issue presentation, you can click on the green "Submit new issue" button to create your issue.

- And that's it! If you choose to comment requesting the issue to be assigned to you, wait for a maintainer to do so. You should get an email notification of the issue being assigned to you or you can view the issue assignment in the issue page. It should look similar to this:

  ![issue assignment](/assets/images/issue_assignment.png)

## Working on an issue

- Please create a separate branch for each issue you work on. Avoid working on multiple issues from the same branch, as this can complicate the review process
- The easiest way to make changes and and test them is by using [![GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/BlackPythonDevs/blackpythondevs.github.io)

- You can also access the Codespaces from the repository main page:

  ![Codespaces tab](/assets/images/codespaces_tab.png)

- The web version of VSCode should open in a new tab in your browser:

  ![Black Python Devs Codespace](/assets/images/blackpythondevs_codespace.png)

## Use UV

[uv](https://astral.sh/uv) is a Python package and project manager.

This project uses uv as it is currently the easiest way for developers with different levels of comfort of Python to quickly and safely get started.

- Install the dependencies. In the terminal, at the project root, open the code editor's terminal and run the command `uv sync --extra dev`.

- Install the pre-commit hooks to automatically format the code before committing. Run the command `pre-commit install`:

  ![Pre-commit install terminal](/assets/images/pre-commit_install_terminal.png)

- After installing the dependencies, its time to run the application. We do this by running the command `uv run render-engine serve`

- The server address shows `http://127.0.0.1:8000`.

> [!NOTE] REMINDER: If using codespaces you will need to forward the port <kbd>Ctrl</kbd> + Click on the Forwarded Address assigned to Port 8000. This will open the running application in a new tab:

![Running page](/assets/images/running_page.png)

### Testing Changes (create new tests as needed)

- Run all tests in the test-suite with the command `uv run python -m pytest`:

  ![Pytest terminal](/assets/images/pytest_run_terminal.png)

### Pushing Changes

- Run `git commit -m "<Your commit message>"` to commit your changes.

  ![Git commit terminal](/assets/images/git_commit_terminal.png)

- Finally run `git push origin <your-branch-name>` to push your changes to your fork.

  ![Git push terminal](/assets/images/git_push_terminal.png)

- Once you’ve committed and pushed all of your changes to GitHub, go to the page for your fork on GitHub, select your development branch, and click the pull request button. Please ensure that you compare your feature branch to the desired branch of the repo you are supposed to make a PR to. If you need to make any adjustments to your pull request, just push the updates to GitHub. Your pull request will automatically track the changes in your development branch and update it. 🥳

## Creating an event

Events are currently created manually by adding entries to `_data/events.json`. To create a conference, use the following JSON structure:

```
{
  "name": "Conference name",
  "url": "https://blackpythondevs.com/",
  "start_date": "2025-02-10",
  "end_date": "2025-09-20",
  "location": "Thailand",
  "description": "Lorem ipsum dolor sit amet consectetur adipiscing elit ...",
  "speaker": "Tim Osahenru"
}
```

### Regular meetups

We have two recurring meetups: **Coffee and Code** and our **Monthly Meetup**. These events remain consistent in format, with only the **date, time, and speaker** subject to change. Updates can be made within the `meetups` list:

```
 {
      "name": "Coffee and Code",
      "date": "2023-09-20",
      "location": "Online (Discord)",
      "description": "A casual meetup for developers to code together.",
      "speaker": "Jay Miller",
      "topic": "Web Development"
    },
    {
      "name": "Monthly meetup",
      "date": "2023-09-20",
      "location": "Remote",
      "description": "Share ideas, and network over coffee.",
      "speaker": "Jay Miller",
      "topic": "Open Source"
    }
```
