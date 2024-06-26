# RCA Ace: Essential RCA Insight Extraction Tool

[![License](https://img.shields.io/github/license/dhi13man/rca_ace)](https://github.com/Dhi13man/rca_ace/blob/main/LICENSE)
[![Contributors](https://img.shields.io/github/contributors-anon/dhi13man/rca_ace?style=flat)](https://github.com/Dhi13man/rca_ace/graphs/contributors)
[![GitHub forks](https://img.shields.io/github/forks/dhi13man/rca_ace?style=social)](https://github.com/Dhi13man/rca_ace/network/members)
[![GitHub Repo stars](https://img.shields.io/github/stars/dhi13man/rca_ace?style=social)](https://github.com/Dhi13man/rca_ace/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/dhi13man/rca_ace)](https://github.com/Dhi13man/rca_ace/commits/main)
[![Build, Format, Test](https://github.com/dhi13man/rca_ace/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dhi13man/rca_ace/actions)

[![Language](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[!["Buy Me A Coffee"](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20an%20Ego%20boost&emoji=%F0%9F%98%B3&slug=dhi13man&button_colour=FF5F5F&font_colour=ffffff&font_family=Lato&outline_colour=000000&coffee_colour=FFDD00****)](https://www.buymeacoffee.com/dhi13man)

RCA Ace is designed for organizations seeking to enhance their understanding and utilization of insights derived from Root Cause Analyses (RCAs). By employing advanced AI techniques, RCA Ace efficiently processes human-written RCAs, extracting key insights, determining root causes, and identifying actionable steps. This tool is pivotal for organizations aiming to optimize their RCA analytics, prioritize actionables effectively, and significantly reduce the time spent on distilling RCA findings.

## Key Features

- **Advanced Insight Extraction**: Employs AI to meticulously extract insights, root causes, and actionable steps from RCAs.
- **Analytics-Ready Data**: Converts unstructured RCA texts into structured, analytics-ready data.
- **Actionable Prioritization**: Facilitates the identification and prioritization of actionable steps, enhancing organizational response to RCAs.
- **Efficiency**: Dramatically reduces the time required to distill and implement findings from RCAs.
- **CSV Export Functionality**: Allows for the easy export of insights into CSV format, streamlining data sharing and analysis.

## Quick Start

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Dhi13man/rca_ace.git
    ```

2. **Navigate to Project Directory**

    ```sh
    cd rca_ace
    ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```sh
   python __main__.py
   ```

## How RCA Ace Works

RCA Ace simplifies the RCA analysis process into a few straightforward steps, starting from reading and cleaning RCA documents, extracting insights using AI, to exporting structured data into CSV files for further analysis.

## Use Cases

### Data Analysis

The structured data extracted by RCA Ace can be used for in-depth data analysis, enabling organizations to identify trends, patterns, and recurring issues across multiple RCAs.

### Actionable Prioritization

RCA Ace helps organizations prioritize actionable steps based on the root causes identified in RCAs, ensuring that the most critical issues are addressed promptly.

This can be done by simply creating pivot tables, graphs, and charts from the structured data to visualize the most common root causes and their corresponding actionable steps.

| Actionable Step Frequencies                                                                                                           | Root Cause Frequencies                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| ![Actionable Step Frequencies](https://github.com/Dhi13man/rca_ace/blob/main/assets/screenshots/actionable_frequency_pivot_table.png) | ![Root Cause Frequencies](https://github.com/Dhi13man/rca_ace/blob/main/assets/screenshots/root_reasons_frequency_pivot_table.png) |

Or create a fancy word cloud to visualize the most common root causes and their corresponding actionable steps.

![Word Cloud](https://github.com/Dhi13man/rca_ace/blob/main/assets/screenshots/action_item_fancy_word_cloud.png)

## Contribution

Contributions are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.

RCA Ace is the tool organizations need to unlock the full potential of their RCAs, ensuring no insight is overlooked and every actionable step is prioritized and implemented efficiently.
