# Financial-Care

Financial Care is a web application developed for social care providers and there staff team to securely store records of the transactions of the people that they support and the staff that have helped them make these transactions

This application has been made alongside HFT Leeds(a social care provider located in leeds). to update there systems and move away from FRS sheets (Paper recording sheets for transactions)

<details>
<summary>Table of Contents</summary>

- [Introduction](#introduction)
- [Rationale](#rationale)
  - [Introduction and Background](#introduction-and-background)
  - [Problems with the Paper Model](#problems-with-the-paper-model)
  - [How This Application Plans to Fix These Issues](#how-this-application-plans-to-fix-these-issues)
  - [Project Scope and Limitations](#project-scope-and-limitations)
  - [Future Versions](#future-versions)
  
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [Organization Goals](#organization-goals)
    - [Managers and Admin Goals](#managers-and-admin-goals)
    - [Staff Member/User Goals](#staff-memberuser-goals)
      - [First-Time User](#first-time-user)
      - [Frequent User](#frequent-user)
      
- [Design](#design)
  - [Imagery](#imagery)
    - [Color Scheme](#color-scheme)
    - [Layout](#layout)
  - [Wireframes](#wireframes)
    - [Changes Since First Designing the Wireframes](#changes-since-first-designing-the-wireframes)
  - [Database Schema](#database-schema)
    - [Database Flow Diagram](#database-flow-diagram)
    - [Changes Since First Designing the Flow Diagram](#changes-since-first-designing-the-flow-diagram)
      - [Staff Fields](#staff-fields)
      - [Many-to-Many Relationship of Service and Staff/Users](#many-to-many-of-service-and-staffusers)
      - [Wallet Entries Fields](#wallet-entries-fields)
  - [Updated Database Flow Diagram](#updated-db-flow-diagram)

- [Features](#features)
  - [Login](#login)
  - [Managers/Admin Controls](#managers-admin-controls)
    - [Services](#services)
    - [Add Service](#add-service)
    - [User Feedback](#user-feedback)
    - [Edit Service](#edit-service)
    - [Add Staff to Service and Remove Staff from Service](#add-staff-to-service-and-remove-staff-from-service)
    - [Delete Service](#delete-service)
    - [Staff](#staff)
    - [Add Staff](#add-staff)
    - [Edit Staff](#edit-staff)
    - [Update Password](#update-password)
    - [Delete Staff](#delete-staff)
    - [Individuals (Service Users)](#individuals-service-users)
    - [Add Individual](#add-individual)
    - [Edit Individual](#edit-individual)
    - [Delete Individual](#delete-individual)
    - [Other Individual Functionality](#other-individual-functionality)
  - [User Controls](#user-controls)
    - [Login as Demo Account (Support Access)](#login-as-demo-account-support-access)
    - [User Services Page](#user-services-page)
    - [User Individuals Page](#user-individuals-page)
    - [User Individuals Page in Specific Service](#user-individuals-page-in-specific-service)
  
  - [Wallet Entries (FRS Sheet Replacement)](#wallet-entries-frs-sheet-replacement)
    - [View Wallet](#view-wallet)
    - [Open Wallet](#open-wallet)
      - [Set Up Wallet](#set-up-wallet)
      - [Check Seal Number](#check-seal-number)
        - [If Seal Number is Incorrect](#if-seal-number-is-incorrect)
        - [If Correct Seal Number is Entered](#if-correct-seal-number-is-entered)
      - [Open Wallet](#open-wallet-form)
      - [Close Wallet](#close-wallet)
        - [Basic Routing Explained: Only Cash Out](#basic-routing-explained-only-cash-out)
        - [Card Out](#card-out)
        - [Withdrawing Cash from Bank](#withdrawing-cash-from-bank)
      - [Routing Functionality](#routing-functionality)
    - [Reconcile](#reconcile)

- [Features Left to Develop](#features-left-to-develop)
  - [Scale](#scale)
  - [Spends](#spends)

- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Manual Testing](#manual-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
    - [Not Storing That Cash Has Been Taken Out](#not-storing-that-cash-has-been-taken-out)
    - [Bug Fix](#bug-fix)
  - [Known Bugs](#known-bugs)

- [Accessibility](#accessibility)
  - [Lighthouse Score](#lighthouse-score)
  - [Browser Testing](#browser-testing)
  - [Device Testing](#device-testing)

- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Programs](#programs)
  - [Frameworks](#frameworks)

- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Resources Used](#resources-used)

</details>


# Rationale

## Introduction and background

To understand this application you must first understand how financial transactions are recorded currently in social care.

Supported people within Social care may not have capacity to look after their own finances. therefore the staff teams that work within these services support the indivdual to to store. withdraw and make payments. 

Cash is usually stored within a wallet or pouch that can be sealed. these seals have a number on them so that the ins and outs of the wallet can be tracked to specific staff members. This is to avoid Financial Abuse or to help identify perptrators of this abuse. These wallets are stored securely in safes that staff have access to.

Whenever a Supported person would like to take money or there bank card out the staff has to access these safes and wallets and Log on a FRS sheet the amount taken out the new total that is left in the wallet and the new seal number that is on the wallet.

Whenever money has been spent by a supported person reciepts have to be logged to the FRS sheet by a staff member and any remaning money has to be added back to the wallet and the new seal number recorded 

FRS sheets are known as Financial Recording sheets and are paper backed documents that record all of these transactions.

Bank statments are usually collected weekly by staff and the FRS sheets updated with transactions such as Direct debits or benefits that have been added to a bank account.

FRS sheets are Legal Documents that are audited by managers and have to reflect every transaction of the indivdual. Staff are to sign for every transaction to state it was them they supported to person to make it.

![FRS sheet](/readme_images/Screenshot%202024-08-23%20085751.png)

## Problems with the Paper Model

There are many issues that arise with FRS sheets that creates more work for Managers and Staff teams that this application aims to solve.

1. Staff members taking money out, recording reciepts and adding money back in and the total of the the reciepts and cash in does not add up to the total of money taken out.
    - This means that there is so money unacounted for. This is classed as a Financial Error for the staff member and can result in disaplinary action.

2. Staff members making addition or subtraction mistakes when adding up the Totals of the wallet or Bank total.
    - This is easily done in a very busy work place but is also a Financial Error.
    - This can cause alot of wasted time when Staff have to reconsile FRS sheets as they have to identify where this error was made.

3. Managers traveling to all services to collect these FRS sheets each month to collect these FRS sheets to be audited.
    - This can take alot of time as services can be spaced far apart.
    - If FRS sheets are not all stored correctly weeks can be missing from this audit.

## How this Application plans to fix these issues.

1. The application will track the cash taken out of a wallet and will prompt a user that the reciepts and cash in does not add up to the cash that was taken out. It will then prompt the user that they are either missing a reciept or to recount the cash going in. if these still do not add up they should contact a manager. (As in procedure Within HFT and other care providers)

2. The Addition and subtraction from the Cash Total and the Bank Account total will be done by the application so that no mistakes are made. The user is only prompted to enter either the cash out, The cash reciepts, the Bank card reciepts or the Cash In.

3. Managers will have access to the Application and can access the records stored digitally and therefore will not need to travel to services to collect FRS sheets.
    - Staff will still store Reciepts but these can be photographed and sent to managers via Email.


## Project Scope and limitations 

The scope of the project includes the development of the web-based application with the aforementioned features, focusing on usability and accessibility. Known limitations include:

- A large orginsation such as HFT has thousands of staff and service users aswell as hundred of services. Querying these large datasets could be slow using Postgresql as the dataset increases. i have proposed some future additions to the application. See Future Versions.

- Social Care providers have to adhere to strict GDPR regulation via the The Data Protection Act 2018. I have set up Encryption with stored passwords however the best practice for a social care provider would be to store these User tables Internally and authenticate through there already set up internal system

The Data should also be stored securly on there in House servers with Access only through the company computers.

## Future Versions

Ideas for future enhancements to WWAMI include:

- An image based upload for Reciepts to be stored on the database with the relating transaction
- Search Bar querying for users, staff and services
- System for logging spends and automating the reciept.
- functionality to edit reciepts before submitting all of them rather than submitting them one by one.


# User Experience (UX)

- ## User Stories

- ### Orginsation Goals

- a. As a orginasation i want the application to save workers time filling out these forms and managers auditing them, allowing for more time spent supporting the people in services.
- b. As a orginsation i want to decrease the amount of financial error that are made while filling out these forms.
- c. As a orginsation i want to be able to ensure these forms are correctly maintained and easily accessable for auditing.

### Managers and Admin Goals

- a. As a manager i want to be able to easily create new services, edit services or delete them to reflect the services i manage.
- b. As a manager i want to be able to easily create new service users and add them to the services that they reside in. Or delete service users that are no longer using us as a care provider.
- c. As a manager i want to be able to easily create new staff members and give them access to the services they are working in. or update the services of exsisting staff members.
- d. As a manager or IT technictan i want to be able to update staff members passwords if they are having trouble logging into the site
- e. As a manager i want to be able to update a staff members access if they have been promoted to a manager.

### Staff member/ User Goals

#### First time user
- a. As a first time user i want to be easily able to access the service that i work in and add records to the person that i am supporting to take money out or in.
- b. As a first time user i want to be easily able to view the records of the person i am supporting.
- c. As a first time user i want the website to be easy to navigate and intutaive as to what i am doing.
- d. As a first time user i want the website to assist with not making any mistakes on the records that i enter.

#### Frequent user
- a. a Frequent user i want to be easily able to access the service that i work in and add records to the person that i am supporting to take money out or in.
- b. a Frequent user i want to be easily able to view the records of the person i am supporting.
- d. As a Frequent user i want to be able to easily view someones records and reconcile bank entries from a bank statment.


# Design.

## Imagery
The imagery and UI wes given great consideration. It needed to be fitting with HFT's other website themes and also be very simple to navigate for staff and managers in order to save time compared to an FRS sheet

### Color scheme

![Color scheme](/readme_images/hft.png)

Hft Website for Example:
![Hft website](/readme_images/hft_website.png)

### Layout 

The Web page has 4 main pages with many sub pages for each Page. 

1. Login- Where the user has to enter there email and password. Note: accounts are created by managers and not by users.

2. Services- The services page displays the user what services they have been allocated to. they can only see these services and no others. Managers can see all services
    - 2.1 Add a service(managers access only) a form to add a service

    - 2.2 Edit a service(managers access only) a form to update or delete a service aswell as viewing staff working in service or removing staff from service

    - 2.3 Add staff to service(managers access only) a form to allocate a staff member to this service

3. Indviduals- this page displays all indivduals a user has access to(as a user may have multiple services they are aloocxated to). this page can also display all indivduals in a specific service if routed through services View people button
    - 3.1 Add a indivdual(managers access only) a form to add a indivdual and asign them to a service

    - 3.2 Edit a indivdual(managers access only) a form to update a indivdual or asign them to another service
    
    - 3.3 Open Wallet(Everyone can access) This routes to multiple pages depending on the record of the indivduals wallet entries
        - No wallet entries -> a form to set up a wallet with cash amount. bank account amount and seal on the real wallet.
        - wallet entry -> a form to declare taking cash or card out and the amounts
        - Cash is out -> a form to record cash reciepts -> a form to record cash back into wallet
        - Cash is out Card is out -> Modal to ask if money has been taken out of bank. If No -> cash reciepts form -> cash in form -> a form to record bank reciepts 
        - Cash is out Card is out -> Modal to ask if money has been taken out of bank. If Yes ->A form to record cash taken out of bank -> cash reciepts form -> cash in form -> a form to record bank reciepts 
        - Only card out -> Modal to ask if money has been taken out of bank. if Yes -> A form to record cash taken out of bank -> cash reciepts form -> cash in form -> a form to record bank reciepts 
        - Only card out -> Modal to ask if money has been taken out of bank. If No -> bank reciepts with entry for seal.
    
    - 3.4 Reconsile Wallet(Everyone can access) This is a form that allows the user to record bank reciepts from a bank statment where they can set the date to the correct date from the bank statement.

4. Staff (manager access only)- All staff members are displayed and can be added, edited or deleted. Passwords can be changed but not stored( for security)

## WireFrames

<details>

 <summary>Services Wireframe</summary>

![Users Wireframe]()

 </details>

 <details>
    <summary>Users Wireframe</summary>

![Users Wireframe]()

 </details>

### Changes since first designing the wireframes.

I have changed alot since first designing the wireframes. Alot of this was due to User testing with Staff members from HFT.

#### Services

Orginally all the infomation about a service was going to be displayed on the services page. The service_users and the staff members. 

i got feedback from staff that they worked in multiple services and so this approach made this page very crowded with infomation. They only ever needed to access the infomation from one service and therefore i decided to route Services into a Indivduals but query for the service ID. this meant that staff would navigate to there service and be able to only see the supported indivduals that they were working with on that shift.

With that infomation i then decided to create all of the main wallet functionality in the drop down for indivduals(service_users)

I also decided to remove the staff members from being viewed directly in Services and moved it to Edit services as the functionality to Add staff to a service or remove staff from a service is only to be used by a manager and edit service can already only be accessed by managers.

## Database flow diagram

<details>

 <summary>Inital DB flow diagram</summary>

![DB flow diagram](/readme_images/financial-care-DBTables.png)

 </details>

## DataBase Schema 

### Changes since first designing the Flow diagram 

#### Many to Many of service and staff/users
The princples are exactly the same. The use of PSQL meant that a seperate refernce table called service_staff is created to hold the many to many relation ship of Staff and Services. therfore Staff/users isnt stored as a foreign key in services 

The name used is also changed to Staff instead of users because querying for users in PSQL gives you the standard PSQL users table that is always created by the program. 

### staff Fields
Email and password(Hashed and salted) were added to the user table. to allow for the login. 

### Wallet entries fields 

three fields were added to Wallet entries

1. Foreign Key of user_id is set as the user that made the entry needs to be tracked for auditing.

2. Is_cash_removed. (Bool) this field was added as a way to track if money was taken out of the last entry and therefore route the user to the forms to put back back in. This is really useful in this application as it makes the UI very simple for staff to use. all they have to do is click Open Wallet button and are routed to the correct form dpending on the last entry of the Indivdual.

3. reciept_number.(int) this field was added as on FRS sheets the reciepts for transactions are numbered by staff which conrespond with the number on the FRS sheet. this means that when managers are reconsiling they are easily able to match the real world reciept with the online recording.

## Updated DB Flow Diagram

I have updated the flow chart to better represent the new Database Schema. 

NOTE: many to many table on flow chart is not an actual table. 

![Updated Schema](/readme_images/Screenshot%202024-08-23%20090508.png)

# Features

## Login

 ### The Login Page requests a users email (all staff have a work email) and a password.

 Users do not sign up to the site. a profile is made by them by a manager at HFT when they first start working.

 ![Login](/readme_images/features/Screenshot%20(111).png)

 ### if a user enters the wrong email or password they are notified 

 ![Incorrect Login](/readme_images/features/Screenshot%20(112).png)

 ### A user Cannot navigate to any other page if not logged in. 


 ## Managers Admin controls

 Managers have access to all services as even though they may manage only a couple they have oncall duties which means that staff members from any service could need there assistance with the software. Therefore they have access to all services,Service Users and users

 ### services

All services are displayed Aswell as additional Add service and edit service buttons

 ![Services managers view](/readme_images/features/Screenshot%20(113).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20142748.png)
 </details>

### Add service
Add service will create a new service. When HFT begins to use this application an IT admin would have to set up all managers user accounts. then managers would go on and add the services they manage.

 ![Add Services managers view](/readme_images/features/Screenshot%20(114).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20143627.png)
 </details>

### User Feedback

Whenever any action is taken on the website that updates the Database or fails to update the database it is shown to the user at the top of the Nav bar with a custom statement and color depending on what action was taken.

 ![User feedback added service](/readme_images/features/Screenshot%20(115).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20144138.png)
 </details>

 #### Users can click this alert to hide it.

 ![User feedback added service hide](/readme_images/features/Screenshot%202024-08-20%20144312.png)

 #### These alerts happen for all actions. here are some examples

 ![User feedback example]()

 Add Examples

 ### Edit Service
 
 Edit Service Allows a manager to change the name of the service. Give staff access to the service and delete the service.

  ![Edit Services managers view](/readme_images/features/Screenshot%20(116).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20144824.png)
 </details>

 ### Add staff to service And Remove staff from service
 If a new staff member starts to work in a service, they will need access to the Service and the people in the service. This is done by the manager filling out this form.
 
 The manager Selects the staff to add and then submits and is redirected back to the edit service page.
  ![Add staff to service managers view](/readme_images/features/Screenshot%20(117).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20145249.png)
 </details>

 #### You can now see the Staff is added to the service and can be just as easily removed via the remove button

 ![remove staff from service managers view](/readme_images/features/Screenshot%20(118).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20145922.png)
 </details>

### Delete Service 

- The Service can be deleted by clicking Delete. it Will show the user a pop up to confirm there actions

- For display purposes we will be deleteing another Service called Service 1 that has two staff members and 2 Indivduals in it

- The Delete function will not delete staff members or service_users accociated with the service.

- Staff can work in multiple services and therfore only there relation to this service is deleted from the link table Service_staff

- Service_users service will be set to none which means that managers can realocate them to a new service when they have moved in to there home 

![delete service managers view](/readme_images/features/Screenshot%20(119).png)

 <details>
 <summary> Mobile View</summary>

 ![service managers mobile view](/readme_images/features/Screenshot%202024-08-20%20151330.png)
 </details>


 ### Staff 

 This page can only be viewed by managers or It admins. 

 ![staff managers view](/readme_images/features/Screenshot%20(121).png)

 <details>
 <summary> Mobile View</summary>

 ![staff managers mobile view](/readme_images/features/Screenshot%202024-08-20%20151946.png)
 </details>

### Add staff

- Initally an Admin account would be set up for and IT personale to add all managers accounts with the access of Manager

- Then Managers can add the current staff that they manage. giving them the "support" access which does not allow admin controls.

- The manager can allocate the staff member a service or leave it blank to later add them to a service when they start working there.

 ![add staff managers view](/readme_images/features/Screenshot%20(122).png)

 <details>
 <summary> Mobile View</summary>

 ![staff managers mobile view](/readme_images/features/Screenshot%202024-08-20%20151946.png)
 </details>

 #### We can now see the new user has been added 

  ![added staff managers view](/readme_images/features/Screenshot%20(124).png)


### Edit staff

- Staff name can be edited

- Staff Acess can be edited if they have been promoted to a manger position 

- Email can be changed in case it was input incorrectly in the first case 

![Edit staff managers view](/readme_images/features/Screenshot%20(127).png)

 <details>
 <summary> Mobile View</summary>

 ![staff managers mobile view](/readme_images/features/Screenshot%202024-08-21%20124928.png)
 </details>

 #### Update Password

 - If a user has forgotten there password. they can call or email a manager and they will reset the users password.
 
 - The forgotten password cannot be recovered only changed.

 ![Update Password staff managers view](/readme_images/features/Screenshot%20(126).png)


### Delete Staff

When trying to delete a staff member a pop up will occur to confirm the deletion 

![delete staff managers view](/readme_images/features/Screenshot%20(128).png)


### Indviduals(Service_users)

Different social care providers call refer to service users as different names. HFT use People we support. others use Supported People or service users. I have used indviduals as this encompasses all and is a generally accepted term for People within supported living or care. 

- This page displays all Service users that someone has access to( managers have access to all)

![Indivduals managers view](/readme_images/features/Screenshot%20(129).png)

 <details>
 <summary> Mobile View</summary>

 ![Indivduals managers mobile view](/readme_images/features/Screenshot%202024-08-21%20125540.png)
 </details>

### Add Indivdual 

- The indivduals name is added

- the bank account they use is set 

- the service they live in is set . This can be left blank if the person does not yet have a service.
    Supported Indivduals only live in one service at a time and that is why this is a one to one conection in the database.

![Add Indivduals managers view](/readme_images/features/Screenshot%20(130).png)

 <details>
 <summary> Mobile View</summary>

 ![Indivduals managers mobile view](/readme_images/features/Screenshot%202024-08-21%20125820.png)
 </details>

 ### Edit Indivdual 

- When editing an indivdual you can change there name 

- You can change the bank account that they use if the person has moved banks 

- You can change the service they are set to. as Supported Indivdual will sometimes move out of one service and start living in another.
    Supported Indivduals only live in one service at a time and that is why this is a one to one conection in the database.
![Edit Indivduals managers view](/readme_images/features/Screenshot%20(131).png)

 <details>
 <summary> Mobile View</summary>

 ![Indivduals managers mobile view](/readme_images/features/Screenshot%202024-08-21%20130706.png)
 </details>

### Delete Indivdual 

A pop up to confirm deletion of indivdual occurs when delete is clicked 

![Delete Indivduals managers view](/readme_images/features/Screenshot%20(133).png)

### Other Indivdual functionality

- The other functionality that links this person to there Wallet entries is accessable by Managers and staff.

- This will be covered in the User Controls functionality portion 

![Edit Indivduals managers view](/readme_images/features/Screenshot%20(132).png)

## User Controls

### Login as Demo account (Support access)

This is now the Section of how staff in services would use the website.

(Password is Shown here for Demo but would be hidden in real application)

![Login support view](/readme_images/features/Screenshot%20(134).png)

### User Services page

- The user only has access to the services that were previously set by the managers 

- The user can be set to multiple service but in this Demo is only set to One

![Services support view](/readme_images/features/Screenshot%20(135).png)

 <details>
 <summary> Mobile View</summary>

 ![Services support view mobile](/readme_images/features/Screenshot%202024-08-21%20132436.png)
 </details>

 #### Users do not have access to the staff tab 

  ![Services support view mobile](/readme_images/features/Screenshot%202024-08-21%20132041.png)

#### If staff member works at multiple services

- I will add a new service that has service users from admin account
- i will link this staff account to that service from admin account 

![Demo second service](/readme_images/features/Screenshot%20(136).png)
![Demo second service](/readme_images/features/Screenshot%20(137).png)

#### Demo user new services Page 

![Demo second service](/readme_images/features/Screenshot%20(138).png)

### user indivduals page

- This page will show all Indivduals a staff member has access to regardless of what service that indivdual is in.

![Indivdual support view](/readme_images/features/Screenshot%20(139).png)

 <details>
 <summary> Mobile View</summary>

 ![Indivdual support view mobile](/readme_images/features/Screenshot%202024-08-21%20133701.png)
 </details>


 ### user indivduals page in specific service. 

 - if the user navigates from Services and clicks view People 

 - it Shows all the service users that are in that specific service 

 - this would be the most common routing to Indivduals page as Staff only tend to work in one service on a shift but will need to make multiple wallet entries for the people in that service.

  ![Indivdual support view ](/readme_images/features/Screenshot%202024-08-21%20133919.png)

 #### This Page is the same as Indviduals but querys for just this service. 

 ![Indivdual support view ](/readme_images/features/Screenshot%20(140).png)

 ## Wallet entries (FRS Sheet replacement)

 ## View Wallet 

 This will show the service users wallet entries 

The User can find this page by clicking on a user and clicking View wallet.

 ![View wallet button](/readme_images/features/Screenshot%20(141).png)

Currently it is empty but you will see that the Fields are the same as an FRS sheet.

![View wallet support button](/readme_images/features/Screenshot%20(142).png)

The Mobile view Displays the fields on the left to fit on a mobile device.
 <details>
 <summary> Mobile View</summary>

 ![Wallet support view mobile](/readme_images/features/Screenshot%202024-08-22%20180054.png)
 </details>
 
## Open Wallet

- Open wallet will route to different forms depending on the previous wallet entries.

### Set Up wallet

If there are no wallet entries then the user is prompted to set up the wallet.

The staff member would count the money in the real world wallet and total in the bank account from a bank statment. They would then seal the pouch and add this number

![Open wallet support button](/readme_images/features/Screenshot%20(143).png)

 <details>
 <summary> Mobile View</summary>

 ![Open wallet support view mobile](/readme_images/features/Screenshot%202024-08-22%20180523.png)
 </details>

 We now see that the wallet is set up 

 ![Open wallet support button](/readme_images/features/Screenshot%20(145).png)

 
 ### Check Seal Number

 If the wallet is set up and a user tries to click Open wallet. they will always be routed to the Check walletg form before continuing. 

 It is HFT policy that the seal number on the real world wallet is checked to be the same as the one previously entered on a FRS sheet before a staff member can make any transactions.

 If the seal number is incorrect then they cannot make any transaction and are to contact a manager. 

 Therefore this check takes place before routing to the forms to add wallet entries. 

 ![Open wallet support button](/readme_images/features/Screenshot%20(146).png)

 #### If Seal number is incorrect

 The user is prompted by a Modal that they should contact a manager if the seal is incorrect and only retry if they typed it wrong.

 ![Open wallet support button](/readme_images/features/Screenshot%20(147).png)

 #### If correct seal number is entered

 The page will route to either Taking cash out or the other routes (Depending on previous entry)

 ### Open Wallet 

 This is a form for the staff member to state. 

 - The description of what they are taking cash or bank card out to do.
 - The amount of cash
 - if the bank card is being taken out 
 - The new seal number after they have sealed the wallet

  ![Open wallet support button](/readme_images/features/Screenshot%20(148).png)

  The staff member would then leave with the supported person and make any transaction with cash. card or get cash out of a bank.


 ### Close Wallet 

 When the last transaction was the previous form of declaring cash or a card is out. when the user clicks open wallet again (When back from a supported trip) the user will be routed to different forms depending on what was taken out 

 This was done to make it very simple for staff to know what needs entering and makes it much harder for them to make a mistake.

 Summary: 
 - If only Cash is taken out then only cash reciepts and cash back in is routed to  

 - if Cash and card are out. the user will be prompted if they have made a cash withdrawl from a bank. it then routes to the same as if only cash is out but with the additional card reciepts form.

 - if Cash has been withdrawn from the bank a form for recording cash out of the bank is recorded before everything else.

 - If the card has been taken out and no cash has been taken out but cash has been withdrawn from the bank. the route works in the same way as cash out and card out.


#### Basic Routing explained Only Cash Out

if you need to see all routes tested then see ![Testing](/TESTING.md)

- The wallet Entry:

  ![Close wallet support button](/readme_images/features/Screenshot%202024-08-22%20183353.png)


1. This Would then show the user check the seal number is correct 

2. This would then show the user Cash reciepts 

  ![Close wallet support button](/readme_images/features/Screenshot%20(150).png)

  - The support worker will enter all the reciepts they have and click done when finished.

  - The page displays the reciept number for the support worker so they can add this to the real world reciept.

  ![Close wallet support button](/readme_images/features/Screenshot%20(151).png)

  - If the Reciept adds up to more than cash taken out the user will be informed 

  ![Open wallet support button](/readme_images/features/Screenshot%20(152).png)

3. The user is then shown a form to enter the remaning cash back into the wallet. 

  - The staff member would now add up the cash they have left and enter the ammount into the form.

  - if this is incorrect. which happens as you can get short changed or loose coins are lost. this modal tells them how much should be going back in and how much they are missing

  ![Close wallet support button](/readme_images/features/Screenshot%20(155).png)

  - They can then add a new reciept if they have forgotten to add one or should look for this missing money. 

  - The wallet can only be closed when this ammount is accounted for 

  ![Close wallet support button](/readme_images/features/Screenshot%20(154).png)

4. The FRS sheet is now populated correctly without any mistakes

  ![Close wallet support button](/readme_images/features/Screenshot%20(156).png)


#### Card out

If only the card is out and no cash is withdrawn from the bank then the user only has to enter bank reciepts. this functionality works the same as cash reciepts without limiting spending. 

![Card wallet support button](/readme_images/features/Screenshot%20(158).png)

![Card wallet support button](/readme_images/Screenshot%202024-08-23%20092204.png)


#### Withdrawing Cash from Bank

If the card is removed then the user always gets prompted first if they have taken any cash from the bank. 

![Card wallet support button](/readme_images/features/Screenshot%20(159).png)

If they have then they fill out the form to say how much has been taken out. 

![Card wallet support button](/readme_images/features/Screenshot%20(160).png)

They will now be sent to Cash Reciepts then Cash in and then Bank reciepts. 

The total Cash withdrawn from the bank is added to the cash that the user could of spent and the cash that needs to go back in 

In This Example £20  was taken out and £100 was withdrawn from the bank.

If the Cash reciept goes over this they are prompted
![Banking wallet support button](/readme_images/features/Screenshot%20(161).png)

Two reciepts are then added:

![Banking wallet support button](/readme_images/features/Screenshot%20(162).png)

If the user enters the wrong ammount. you can see that the Total is tracked

![Banking wallet support button](/readme_images/features/Screenshot%20(163).png)

the same happens for a total above 

![Banking wallet support button](/readme_images/features/Screenshot%20(164).png)

The user can then add any bank reciepts if they spent money using the card( not the Withdrawl)

![Banking wallet support button](/readme_images/features/Screenshot%20(165).png)

You can see the Wallet entries here 

![Banking wallet support button](/readme_images/Screenshot%202024-08-23%20092229.png)


#### Routing functionality

The other inputs work exactly in the same way. i have outlined all forms. different ones are shown to the user depending on what they took out orginally and the decision on the baking modal. 

I covered all the cases how staff would support people out.

If they just pay using the card or just with cash. if they go to the bank and withdraw cash to then spend. if they sepnd on the card and with cash. or all of the above. 


## Reconcile 

Usually in HFT services. a staff member will collect bank statements weekly and then Reconsile the FRS sheet so that the total of the real world bank account matches the total of the FRS sheet count. The reason they dont match up is because of standing orders, benefits. Any automatic payments that are not made by staff.

- Therefore when reconsiling the Date of this transaction is needed

- There also needs to be a way to put cash into the bank for things such as Benfits or family sending money. 

The User picks if it is Cash in or cash out 

![Reconsile wallet support button](/readme_images/features/Screenshot%20(141).png)

They can then Add these transactions in and the Bank total will be updated. 

![Reconsile wallet support button](/readme_images/features/Screenshot%20(167).png)
![Reconsile wallet support button](/readme_images/features/Screenshot%20(169).png)

# Testing 

## Validator Testing

## Manual Testing 

- I have manually tested all CRUD functionality of the tables. staff, service_users, services, Wallet_entry and the many to many link table of service_staff. All buttons and routes work correctly and the change in the database is immediately refelected on the website. 

- I have manually tested that all CRUD functionality displays a alert to the user. to notify them of what action has taken place.

- I have tested that any delete functionality will prompt the user before allowing them to remove a object. 

- I have tested the routing system for wallet_entry (Open Wallet button) to make sure that it routes to the correct form depending on what the user filled out in the Cash out form and the modal for banking. 

- I have tested that the website does not allow users to enter cash reciepts and cash in that does not add up to the inital cash out. 

Testing document : [Testing](/TESTING.md)

## User Testing 

I have had my collegues that work in Social care and use FRS sheets on a daily basis to test the difference between the two and give me feedback on what they think of the application.



## bugs 

### Not storing that Cash has been taken out

The Open Wallet route should redirect to a form to add reciepts if cash has been taken out.

if the user takes cash out and then enters the reciepts in but does not click "done" to be redirected to the add cash in page the open wallet button will then redirect them back to taking cash out even though the cash may still need to be entered into the wallet. 

Example:

1. Cash taken out 
![Cash out Example](/readme_images/cash_out_example.png)

2. Adding reciept
![reciept added example](/readme_images/add_reciept_example.png)

3. Confimation of new reciept 
![reciept added example](/readme_images/reciept_added_example.png)

4. User Error - They click a navigation link, logout or close browser.
![User error example](/readme_images/user_error_example.png)

5. The Bug - redirecting to Take cash out form 
![Bug example](/readme_images/open_wallet_redirect_example.png)

6. The Data added to the database 
![Database data](/readme_images/wallet_entries_incorrect_example.png)


#### bug fix 
To fix this i needed to change the Model of wallet_entry table to add a is_cash_out boolean field. similar to the is Card out field. 

The reason for doing this instead of just using the stored Session data is that if another user has made this mistake and another user is left to fix it. they will be unable to as the data is stored only on a session.

This will also be a useful feature as sometimes in social care. the person that has taken cash out for a service user might finish shift as they come back with the reciepts. and another satff member will enter them in. 

![Fix Image](/readme_images/fix1.png)
![Fix Image](/readme_images/fix2.png)
![Fix Image](/readme_images/fix3.png)
![Fix Image](/readme_images/fix4.png)
![Fix Image](/readme_images/fix5.png)



This still has the issue of not adding the previously stored reciepts which can be fixed by querying and totaling them to create the new Outstanding total that is passed to CloseWallet. (the reciepts form)

```python
if last_wallet_entry.is_cash_removed == True or last_wallet_entry.bank_card_removed == True:
        last_wallet_entry = WalletEntry.query.filter(
        WalletEntry.service_user_id == service_user_id,
        WalletEntry.cash_out > 0).order_by(WalletEntry.id.desc()).first()

        subsequent_entries = WalletEntry.query.filter(
        WalletEntry.service_user_id == last_wallet_entry.service_user_id,
        WalletEntry.id > last_wallet_entry.id,  
        WalletEntry.is_cash_removed == True ).all()

        if subsequent_entries:
            cash_spent_values = [entry.cash_spent for entry in subsequent_entries]
            total_cash_spent = sum(cash_spent_values)
        else:
            total_cash_spent = 0
        

        result = last_wallet_entry.cash_out - total_cash_in

        return redirect(url_for("close_wallet",service_user_id=service_user_id,last_wallet_id=last_wallet_entry.id,outstanding_money=result))
```

Evidence of fix 

![Final Fix](/readme_images/final_fix.png)


# Known Bugs 

There are no known bugs

# Accessibility

## lighthouse score

## Browser testing 

- The Website was tested on Google Chrome, Firefox, Microsoft Edge, Safari browsers with no issues noted.  

## Device Testing 

- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, iPhoneX and iPad to ensure responsiveness on various screen sizes. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

# Technologies used:

## Languages:
- HTML5
- CSS3
- JavaScript
- Python
- Jinja2 

## Frameworks, librarys and programs used. 

### Programs
- Chrome dev tools- used for overall development and testing, including responsivness and preformance
- GitHub -Used for version control 
- W3C -used for validation testing of HTML and CSS

### Frameworks
- Flask-SQLAlchemy- used for the back end Routing and data manipulation 
- PostgreSQL - used to store and manage the database.

# Deployment

# Features left to develop 

## Scale.

As HFT is split up into sectors. the Database currently only has to store all the services in one sector. However. if HFT was to adopt this across all Sectors then there Would need to be a system in place to handle the larger amount of data. especially when an Admin is using the Services and Users pages.

This is because these pages currently display all services and all users. Having a search bar would help managers find people or services yes, however if this was adopted on scale then displaying all services and users could take alot of time and therefore the data should be split into sectors/areas. 

This could be achived by adding Area field to services and users. then displaying only services and users from that area. an additional form would then be added to the top of services and users giving an option to change the area. 

## Spends. 

Some Social care providers do not require reciepts for transactions called spends,where the supported person is given an amount of money to spend on there own without staff present. a extra tile on the cash out form could be added to specify spends. this would then automatically complete this as a whole transaction and not route the user to add a reciept when opening the wallet

# Credits

## Content 

I currently work in Health and social care and therefore have noticed the issues with the FRS sheets personally and from staff and managers. There seems to be alot of time wasted with very small mistakes. when something is being used as often as this is. it should be efficent and difficult for users to make these mistakes. 

i Built this website for my workplace and as i have friends thats work in other charities that deliver social care. i would like to continue developing it and deliver it to these other businesses to help fix these issues. 

## Resources Used 

