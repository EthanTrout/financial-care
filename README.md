# Financial-Care

Financial Care is a web application developed for social care providers and there staff team to securely store records of the transactions of the people that they support and the staff that have helped them make these transactions

This application has been made alongside HFT Leeds(a social care provider located in leeds). to update there systems and move away from FRS sheets (Paper recording sheets for transactions)


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

 ### Edit Service (Update Images to new color)
 
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


# Testing 

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