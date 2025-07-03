
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
- update a member information the system.
- View a member’s full subscription history.
- Add a subscription to a specific member (Silver, Gold, or Diamond).
- Suspend a member’s active subscription.
- Reactivate a suspended subscription with time compensation.
- Automatically mark expired subscriptions based on dates.
- View all system data (members + subscriptions).
- Save and load all data from a JSON file automatically.
- Exit the system safely without data loss.
## 🔧 Usage Instructions

Once you run the system, you'll see the following main menu options:

### 🏠 Main Menu

1 - Add new gym member  
→ Register a new member by entering their ID, name, and birth date. The system ensures IDs are 4 digits and unique.

2 - Display all members  
→ Shows a list of all registered members with their personal details (ID, name, birth date, age).

3 - Delete a member  
→ Enter a member's ID to permanently remove them from the system.

4 - Update member information  
→ Modify a member's ID, name, or birth date.

5 - Search for a member to manage subscriptions  
→ Enter a member's ID to view and manage their subscriptions:  
  1. Add new subscription (Silver / Gold / Diamond)  
  2. View subscription history  
  3. Suspend membership  
  4. Reactivate membership  
  5. Return to main menu

6 - Display Everything in the system  
→ View all members along with their full subscription history.

7 - Exit  
→ Safely close the application and save all changes to the JSON file.

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
