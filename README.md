# OOB-ticketingSystem

Railway Booking Credit System for Chinese Spring Festival(By Chenghong Meng)

Background: Chunyun also referred to as the Spring Festival travel season or the Chunyun period, is a period of travel in China with extremely high traffic load around the time of the Chinese New Year. The period usually begins 15 days before Lunar New Year's Day and lasts for around 40 days. The number of passenger-journeys during the Chunyun period is projected to be hitting over 2.9 billion in 2016. It has been called the largest annual human migration in the world. Rail transport experiences the biggest challenge during the period, and myriad social problems have emerged. Huge profits and demands have also created ticket scalpers, which is a common name for people who profit by specializing in selling tickets at a marked-up price. Because of ticket scalpers, many people can't get tickets or have to buy expensive tickets from ticket scalpers. In order to solve the problem of tickets scalpers, a real-name ticket purchasing system has been implemented since 2010, which requires passengers to present a valid ID when purchasing a train ticket and then to show the same ID when checking in for a train. In some ways, the real-name system plays a role in combating the illegal re-sale of tickets during the ’spring rush’, and it has at least taken some of the misery out of the travel period, but the problem not be solved completely. There are still a lot of ticket scalpers in many train station, Why?
Problem with old system: One passenger could buy same trips for continually dates; Without credit system, then has no way to track user behavior, then were not able to identify  scalpers; Has no way check ticket status, leaving a bug for scalpers and malicious passengers.

The vision of new system: with this new system, user could order trips for passengers; passenger could return their ticket before valid date and get partial refund; system could monitor purchase behavior and identify ticket scalper and ticket evader. Administrator can manage those accounts’ problems. Details about its capabilities should include:
1. Query Trips: System allow users or non-users to query trips and fares for up to 40 days. System will display all possible routes, train of class, starting time, ending time,  by-pass station, seats left and fares. 
2. Order Trips:  
    •	System only allow real-name users with valid ID to create a profile and to  order trips. System will have right to verify the authority of users’ ID.
    •	System allow regular users to order multiple trips for multiple passengers by providing real passenger name. 
    •	For same passenger, system does not allow to order same trip for consecutive days, unless exempted. 
    •	For same date, system does not allow same passenger to order two or more unreasonable trips.
    •	Order history could be checked, stored, and download. 
    •	System will determinate users’ account to be status of ‘Normal’, ‘Watching’, ‘Warning’, and ‘Suspend’ according the purchase and return behavior, grade credit score. 
    •	System allow user reset their password.
    •	System allow user to have 30 mins to hold their order.
    •	System allow user to cancel their order, allow passenger return ticket before valid date.
3. Ticket:
    •	Each ticket will represent all information about this trip, train, starting time, ending time, starting station, ending station, seat, and the passengers real- name  and ID number. 
    •	Each ticket will generate a QR code, which will help system track the status of this ticket.
4. Return and Refund: 
    •	System allow users to revoke orders before ticket was generated; after ticket was generated, only passenger was allow to return ticket and get partial refund before trips. 
    •	System will determinate refund ratio according to passenger credit score.  
5. Credit Score:
    •	System analysis users and passenger order and return behavior, predict credit score.
    •	Users allow to check their own credit. 
    •	Credit can not be transferred. 
    •	System will assigned different purchase and return authority to different status of account.
6. Account Management:
    •	Administrator can login and manage all customers’ accounts
    •	Administrator can be contacted with email, phone, and online chat at certain timeframe for account issues.

