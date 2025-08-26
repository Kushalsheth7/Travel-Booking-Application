Assignment: Travel Booking Application
Objective:
Build a simple travel booking web application using Python (Django) that allows users to view
available travel options, book a ticket, and manage their bookings. The frontend can be
developed using Django templates.
Requirements:
Backend:
1. User Management:
○ Implement user registration, login, and logout using Django's built-in
authentication system.
○ Allow users to update their profile information.
2. Travel Options:
○ Create a model for Travel Options (e.g., flight, train, bus), which includes fields
such as:
■ Travel ID
■ Type (Flight, Train, Bus)
■ Source
■ Destination
■ Date and Time
■ Price
■ Available Seats
3. Booking:
○ Allow users to book travel options by selecting a travel option, entering details,
and confirming the booking.
○ Each booking should be stored in a Booking model, which includes:
■ Booking ID
■ User (Foreign Key)
■ Travel Option (Foreign Key)
■ Number of Seats
■ Total Price
■ Booking Date
■ Status (Confirmed, Cancelled)
4. View and Manage Bookings:
○ Users should be able to view their current and past bookings.
○ Implement functionality to allow users to cancel bookings.
Frontend:
1. User Interface:
○ Design simple but user-friendly pages using Django templates.
○ Create views for:
■ User registration, login, and profile management.
■ Listing available travel options with filters for type, source, destination,
and date.
■ Booking form for selecting travel options and confirming the booking.
■ Displaying current and past bookings with options to cancel bookings.
2. Responsiveness:
○ Ensure the pages are responsive and functional across devices (e.g., desktop,
mobile).
3. Styling:
○ Use CSS to style the pages. You can also use a framework like Bootstrap for
faster development.
Bonus Points:
● Use MySQL as the database for the project.
● Implement basic validation (e.g., user input, number of available seats).
● Write unit tests for critical features.
● Add search and filtering capabilities for travel options (e.g., filter by type, date, or
destination).
Submission:
● Push the code in a GitHub repository.
● Provide instructions in the README file on how to set up the project locally.
● Deploy the application to google cloud platform and share
the deployed URL.
Evaluation Criteria:
● Backend functionality and adherence to Django best practices.
● Frontend usability, design, and responsiveness.
● Code quality and structure.
● Use of MySQL and any cloud deployment (if applicable).
● Problem-solving skills and creativity.