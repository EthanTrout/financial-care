# Bugs 

## psql user table

minor bug i found when creating a user table was that psql already created a user table so when doing SQL statements in the terminal i could not view user table. i migrated my model to be called Staff instead of user to avoid this interaction



# Testing 

## Admin/ Manager Functionality:

### CRUD User

#### Creating and viewing User

1. The current users are populated to the page only for admins 
    ![Users page](/readme_images/Testing_images/users/users_tab.png)

2. A new user details are added leaving service blank as no services are yet created
    ![New User page](/readme_images/Testing_images/users/add_users_tab.png)

3. The new user is displayed correctly on the users page
    ![Users page updated](/readme_images/Testing_images/users/new_user_created.png)

4. Evidence of new user being added to database (Passwords are stored in Hashes with salt)
    ![Database updated](/readme_images/Testing_images/users/staff_database.png)

5. User must fill in forms to complete
    ![Database updated](/readme_images/Testing_images/users/users_auth.png)


#### Updating User and new password

1. Admin can update User infomation and change password if forgotten. 
    ![update user](/readme_images/Testing_images/users/update_user.png)

2. New user details changed 
    ![update user](/readme_images/Testing_images/users/update_user_tab.png)

3. Evidence new user Updated 
    ![users page updated](/readme_images//Testing_images/users/update_user_updated.png)

4. Password can only be changed.
    ![users password updated](/readme_images//Testing_images/users/user_password_changed.png)

5. Evidence for user password changed. 

#### Deleting user 

1. User delete button Confirm
    ![users delete Modal](/readme_images//Testing_images/users/user_delete_modal.png)

2. Evidence Of change
    ![user deleteted](/readme_images//Testing_images/users/user_deleted.png)
    ![user deleteted database](/readme_images//Testing_images/users/user_deleted_database.png)


### CRUD service and Service_staff

#### Creating a new service 

1. Services Displayed on services Tab (none yet created)
    ![Services](/readme_images/Testing_images/services/services_tab.png)

2. New Service page (Only admins can create new services)
    ![New Service](/readme_images/Testing_images/services/create_service_tab.png)

3. Evidence of new service Added
    ![Services Updated](/readme_images/Testing_images/services/new_service_added.png)


#### Updating Service , Adding and removing Staff from many to many Service_user

1. Edit service page (Only managers and admins) 
    ![Edit Service](/readme_images/Testing_images/services/edit_service_tab.png)

2. Adding New staff member to Service
    ![Added staff](/readme_images/Testing_images/services/add_staff_to_service.png)
    ![Added staff](/readme_images/Testing_images/services/staff_added_to_service.png)

3. Removing Staff member from service Modal
    ![Removed staff](/readme_images/Testing_images/services/removing_staff_from_service.png)
    ![Removed staff](/readme_images/Testing_images/services/staff_removed_from_service.png)

4. Services of staff member also displayed on staff page 
    ![Added staff service](/readme_images/Testing_images/services/staff_page_show_services.png)

5. Deleting Service
    ![deleting service](/readme_images/Testing_images/services/deleting_service.png)
    ![deleting service](/readme_images/Testing_images/services/deleted_service.png)


### CRUD service_users/indivduals 

#### Displaying and creating service Users
1.  Displaying Service users (none currently added)
    ![service_users page](/readme_images/Testing_images/service_users/service_users_tab.png)

2. Adding service users (I have added multiple for testing purposes)
    ![add service_users page](/readme_images/Testing_images/service_users/add_service_user.png)
    ![added service_users ](/readme_images/Testing_images/service_users/added_service_users.png)

3. Viewing all service_users in a service
    ![added service_users ](/readme_images/Testing_images/service_users/view_people_in_service.png)
    ![added service_users ](/readme_images/Testing_images/service_users/people_in_service.png)

4. You can also View All service users that you have access to in the Indivdual tab
    ![view service_users ](/readme_images/Testing_images/service_users/view_all_people.png)

#### Updating and deleting service_users

1. Editing Service User
    ![updating service_users ](/readme_images/Testing_images/service_users/edit_service_user_button.png)
    ![editng service_users tab ](/readme_images/Testing_images/service_users/edit_service_user_tab.png)
    ![Updated service_users ](/readme_images/Testing_images/service_users/edited_service_user.png)
    
2. Deleting Service User 
    ![deleting service_users ](/readme_images/Testing_images/service_users/deleting_service_user.png)
    ![deleted service_users ](/readme_images/Testing_images/service_users/deleted_service_user.png)



## User Functionality

### Login and Logout

1. User feedback when password is incorrect
    ![Login incorrect](/readme_images/Testing_images/login/login_incorrect.png)
    ![Login incorrect](/readme_images/Testing_images/login/login_incorrect_feedback.png)

2. Accessing other pages without logging in cannot be done.
    ![Accessing pages without login](/readme_images/Testing_images/login/login_redirect_to_login.png)

3. Logging out clears a session and redirects back to login

### Access

1. New_user we created before login 
    ![new user login](/readme_images/Testing_images/login/new_user_login.png)

2. Users service page has only access to the services that they are asigned to and the indivduals that are in that service 
    ![New user services page access](/readme_images/Testing_images/login/new_user_services_page_access.png)
    ![New user services page access](/readme_images/Testing_images/login/new_user_people_page_access.png)

3. For Refernce Admins can access all services and all indviduals
    ![New user services page access](/readme_images/Testing_images/login/admin_login.png)
    ![New user services page access](/readme_images/Testing_images/login/admin_service_page_access.png)

4. users cannot Acess any of the previously defined admin CRUD functionality

### service_user Wallet

#### Set up

1. Viewing Wallet
    ![View Wallet](/readme_images/Testing_images/wallet/viewing_wallet.png)
    ![View empty Wallet](/readme_images/Testing_images/wallet/empty_wallet.png)

2. Setting up an empty wallet- if the service_users wallet is empty a user is redirected to set up wallet 
    ![set up Wallet](/readme_images/Testing_images/wallet/setting_up_wallet.png)
    ![set up Wallet](/readme_images/Testing_images/wallet/set_up_wallet.png)

3. Testing Inputs:
    User cannot input strings into the form. this could be broken by using something such as postman API online:
    This would return an error. it would not allow a string to be added to the database.

    Form Notifies users if number is not decimal 
    ![Number not decimal](/readme_images/Testing_images/wallet/wallet_number_not_decimal.png)

    Max Length is set.
    ![Max Length](/readme_images/Testing_images/wallet/wallet_max_length.png)
    

#### Check Seal
Before a user can take enter a wallet they must verify that the seal on the real world wallet matches the last one entered in the system

1. Check Seal Form 
    ![Check Seal](/readme_images/Testing_images/wallet/Check_seal.png)

2. If incorrect:
    ![check seal incorrect](/readme_images/Testing_images/wallet/Check_seal_incorrect.png)

3. User has to enter a number and cannot enter a string as HTML is set to number 

4. If correct 
    ![ seal number stored](/readme_images/Testing_images/wallet/seal_number_stored.png)
    ![ seal number entered](/readme_images/Testing_images/wallet/seal_number_entered.png)

#### Taking Cash out. Adding Cash reciepts. Adding Cash back into wallet

When user clicks Open Wallet if no cash is out they will be directed to take cash out.

1. Take Cash out 
    ![cash out](/readme_images/Testing_images/wallet/take_cash_out_only_cash.png)

2. Confirmation of Cash out 
    ![cash out](/readme_images/Testing_images/wallet/take_cash_out_only_cash_view.png)


The User would now be out with a supported person and make payments with this cash 

3. Cash Reciepts 
    ![cash Reciept](/readme_images/Testing_images/wallet/cash_reciepts_added.png)
    ![cash Reciept](/readme_images/Testing_images/wallet/cash_reciepts_added_2.png)

4. if cash reciepts added go over cash taken out 
    ![cash Reciept over](/readme_images/Testing_images/wallet/cash_reciept_over.png)
    ![cash Reciept modal](/readme_images/Testing_images/wallet/cash_reciept_modal.png)

The user then clicks done and is prompted to put cash in 

5. Cash back in 
    ![cash in ](/readme_images/Testing_images/wallet/cash_in.png)
    ![cash in ](/readme_images/Testing_images/wallet/cash_in_view.png)

6. If can in is over or under the remaning money to put it in notifies staff 
    ![cash in over](/readme_images/Testing_images/wallet/cash_in_over.png)
    ![cash in over](/readme_images/Testing_images/wallet/cash_in_over_modal.png)

    ![cash in under](/readme_images/Testing_images/wallet/cash_in_under.png)
    ![cash in under](/readme_images/Testing_images/wallet/cash_in_under_modal.png)


#### Taking Cash out. Taking card out . adding cash reciepts. adding cash back in. adding bank reciepts.

1. Cash and Card Out 
    ![Cash out and card out](/readme_images/Testing_images/wallet/cash_out_card_out/cash_out_card_out.png)

2. Card Out Modal for if staff has gone banking 
    ![Card out Modal](/readme_images/Testing_images/wallet/cash_out_card_out/card_out_modal_banking.png)

3. User has clicked No. cash reciepts in 
    ![cash reciepts](/readme_images/Testing_images/wallet/cash_out_card_out/cash_out_card_out_cash_reciepts.png)

4. Cash in 
    ![cash in](/readme_images/Testing_images/wallet/cash_out_card_out/cash_out_card_out_cash_in.png)

5. Bank Reciepts 
    ![bank reciepts](/readme_images/Testing_images/wallet/cash_out_card_out/cash_out_card_out_bank_reciepts.png)
    ![bank reciepts](/readme_images/Testing_images/wallet/cash_out_card_out/cash_out_card_out_bank_reciepts2.png)
    

6. Viewing results 
    ![View FRS](/readme_images/Testing_images/wallet/cash_out_card_out/cash_out_card_out_view.png)


#### Cash Out. Card Out . Taking withdrawing cash from bank. adding cash reciepts. adding cash back in . adding bank reciepts 

Staff members may support someone out to Get cash out of the bank. money may be spent with the cash and this needs to be tracked when putting the cash back in.

1. Shopping and banking 
    ![shopping and banking](/readme_images/Testing_images/wallet/cash_out_card_out_banking/shopping_banking.png)

2. Banking Modal 
    ![banking modal](/readme_images/Testing_images/wallet/cash_out_card_out_banking/banking_modal.png)

3. Cash Withdrawl from Bank
    ![withdwal from bank](/readme_images/Testing_images/wallet/cash_out_card_out_banking/cash_out_of_bank.png)

4. Cash reciepts
    ![cash reciepts](/readme_images/Testing_images/wallet/cash_out_card_out_banking/cash_reciepts.png)

5. Cash In Modal- updated with the cash withdrawl from bank 
    ![cash in modal](/readme_images/Testing_images/wallet/cash_out_card_out_banking/cash_in_incorrect.png)

6. correct cash in 
    ![cash in](/readme_images/Testing_images/wallet/cash_out_card_out_banking/cash_in_correct.png)

7. bank card reciepts
    ![bank reciepts](/readme_images/Testing_images/wallet/cash_out_card_out_banking/bank_reciepts.png)

8. viewing results
    ![results](/readme_images/Testing_images/wallet/cash_out_card_out_banking/shopping_banking_result.png)

#### Card Out. Withdraw cash from bank. cash reciepts. cash in 

A service_user may have no cash to take out and therefore they withdraw cash from a bank before spending cash 

1. Card Out only
    ![](/readme_images/Testing_images/wallet/card_out/card_out.png)

2. Banking Modal
    ![](/readme_images/Testing_images/wallet/card_out/banking_modal%20(2).png)

3. Withdrawing from bank
    ![](/readme_images/Testing_images/wallet/card_out/card_banking.png)

4. Cash Reciepts
    ![](/readme_images/Testing_images/wallet/card_out/card_cash_reciepts.png)

5. Updated Cash in to show cash withdrawn from bank 
    ![](/readme_images/Testing_images/wallet/card_out/card_cash_in_incorrect.png)

6. Cash in
    ![](/readme_images/Testing_images/wallet/card_out/card_cash_in_correct.png)

7. Bank reciepts is now shown to user but as none need enetering user clicks done 

8. Results
    ![](/readme_images/Testing_images/wallet/card_out/card_results.png)


#### Conclusion of user Wallet Functionality Testing:

I have concluded that all routes correctly redirect the user to the correct form depending on there inital Cash out record and then there input of the banking Modal.

I think that this is a very good way to make it easy for staff members to not make mistakes when recording wallet entries. If i was to rather implement a system that just allowed users to click cash in and cash out then human errors are more likely to be made. This way if cash is out then tthe user is propmted to deal with this entry before moving on to anything else.