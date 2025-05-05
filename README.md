# Fake Review Monitoring System – UI Interaction

With the rapid growth of online shopping on various e-commerce platforms, users increasingly rely on ratings and reviews to judge product quality. At the same time, the prevalence of fake reviews undermines trust in both the products and the platform. Conversely, negative fake reviews can harm merchants’ reputations and sales. To address these challenges, we have extended the work from anubhavs11’s Fake-Product-Review-Monitoring by integrating a user interface that supports the following scenarios:

New User/Admin Registration
– A simple form for signing up, with separate roles and permissions for users and administrators.

User Review Submission
– Registered users can write and submit product reviews through an intuitive UI.

Admin Alert on Suspicious Reviews
– Administrators receive real-time notifications when a review is flagged as potentially fake.

Invalid Credentials for Users
– If a user enters incorrect login details, the system displays an “Invalid credentials” prompt.

Blocked or Bot User Login Attempt
– Blocked accounts or detected bots receive a “You are blocked” message when they try to log in or post a review.

Admin Analytics Dashboard
– Administrators can interact with the UI to view summary statistics, visualizations, and detailed analyses of review authenticity.

Invalid Credentials for Admins
– Admin login attempts with wrong credentials trigger the same “Invalid credentials” prompt, ensuring consistency.

Invalid File Upload Handling
– When a non-CSV file is uploaded (e.g., .txt, .xlsx), the UI returns an “Unsupported file format” error, guiding users to provide the correct .csv input.
