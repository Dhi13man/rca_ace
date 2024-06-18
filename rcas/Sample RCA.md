# Root Cause Analysis (RCA) Document

## Topic: Number of days till Bill Due was wrongly shown in View all Bills Screen

### Introduction

On June 17, 2024, it was discovered that the "View all Bills" screen in our billing application was displaying an incorrect number of days until the bill due date. This issue has caused confusion among users, leading to potential late payments and a loss of trust in our system. This document outlines the impact, root causes, immediate fixes, long-term solutions, learnings, and actionables to prevent such issues in the future.

### Impact

- **Customer Confusion:** Customers were misled by the incorrect due dates, resulting in confusion and frustration.
- **Late Payments:** Some users may have missed their payment deadlines, incurring late fees.
- **Trust Erosion:** The reliability of our billing system has been called into question, potentially harming our reputation.
- **Increased Support Tickets:** Customer support experienced a spike in tickets related to billing date discrepancies.

### 5 Whys

1. **Why** was the number of days till bill due wrongly shown?
   - The calculation logic for the due date display was incorrect.

2. **Why** was the calculation logic incorrect?
   - The date difference function used the system's local date instead of the server date.

3. **Why** was the system's local date used instead of the server date?
   - The local date was hardcoded into the billing module due to a previous quick-fix for a timezone issue.

4. **Why** was a quick-fix solution implemented without thorough testing?
   - There was a tight deadline for a minor release, and the fix was deemed low-risk.

5. **Why** was the risk of the fix underestimated?
   - Lack of a comprehensive testing framework and insufficient code review processes.

### Immediate Fix

- **Corrected the Date Calculation Logic:** Updated the code to ensure the server date is used for all date calculations related to bill due dates.
- **Hotfix Deployment:** A hotfix was promptly deployed to rectify the issue on all production servers.

### Long Term Fix

- **Refactor Date Handling Code:** Review and refactor the date handling logic across the entire billing system to ensure consistency and accuracy.
- **Implement Comprehensive Testing:** Develop and implement a robust testing framework, including unit tests and integration tests specifically for date and time calculations.
- **Enhance Code Review Process:** Establish a more stringent code review process to catch potential issues before they reach production.

### Learnings

- **Importance of Consistent Date Handling:** Ensuring that date and time calculations are consistent and accurate is crucial for user-facing applications.
- **Risk of Quick Fixes:** Quick-fix solutions, especially those involving core functionalities like billing, can lead to significant issues if not properly tested.
- **Value of Thorough Testing:** Comprehensive testing, including edge cases and system-wide impact, is essential to maintain the reliability of the application.

### Actionables

1. **Develop a Date Handling Standard:** Create a standard for date and time handling across all modules and enforce its use.
2. **Training for Developers:** Conduct training sessions for developers on the importance of proper date handling and the risks of quick fixes.
3. **Enhanced Testing Protocols:** Introduce enhanced testing protocols for all releases, including mandatory test cases for date and time calculations.
4. **Regular Code Audits:** Schedule regular code audits to ensure adherence to best practices and identify potential issues proactively.
5. **Customer Communication:** Inform affected customers about the issue, the steps taken to resolve it, and any actions they may need to take.

By addressing these points, we aim to prevent a recurrence of this issue and enhance the reliability and trustworthiness of our billing system.
