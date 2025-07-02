
Gym Membership System 

overview:
A gym management system that helps manage gym members and their subscriptions. This system has two main roles: the user (staff/manager) who operates the system and the gym member whose data is being managed.
The system allows the manager to register new members, assign subscriptions, and track member status easily.

Features & User Stories:

As a gym manager I should be able to do the following:
- Add a new gym member.
- View a list of all current members.
- Search for a specific member by their ID.
- Delete a member from the system.
- View a member’s full subscription history.
- Add a subscription to a specific member (Silver, Gold, or Diamond).
- Suspend a member’s active subscription.
- Reactivate a suspended subscription with time compensation.
- Automatically mark expired subscriptions based on dates.
- View all system data (members + subscriptions).
- Save and load all data from a JSON file automatically.
- Exit the system safely without data loss.

usage : 
Type 1 - Add a new member
→ Enter the member's ID, name, and birth date to register them in the system.

Type 2 - Show all members
→ Displays a list of all current gym members with their details.

Type 3 - Delete a member
→ Enter the member's ID to remove them completely from the system.

Type 4 - Search and manage a member
→ Enter the member’s ID. If found, you can:
   1 - Add a new subscription (Silver / Gold / Diamond)
   2 - View subscription history
   3 - Suspend the membership
   4 - Reactivate suspended membership
   5 - Return to main menu

Type 5 - Show everything
→ Shows all members along with their full subscription history.

Type 6 - Exit
→ Closes the application safely.

------------------------------------
Notes:
• Data is saved automatically to 'gym_data.json'.
• Membership statuses:
   - activate = Active
   - suspend = Temporarily paused
   - expired = Ended and not renewed
• Payment methods: Cash or Card.
• Subscription plans:
   - Silver = 200 SAR/month
   - Gold = 300 SAR/month
   - Diamond = 400 SAR/month
------------------------------------
