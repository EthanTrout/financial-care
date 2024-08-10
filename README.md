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



