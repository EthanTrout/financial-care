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


## Testing User Functionality