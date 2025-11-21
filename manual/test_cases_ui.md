# UI Test Cases – SauceDemo

## TC_UI_01 – Valid Login

**Module:** Login  
**Priority:** High  

| Field         | Details                                                              |
|---------------|----------------------------------------------------------------------|
| Test Case ID  | TC_UI_01                                                             |
| Title         | Login with valid standard user                                       |
| Precondition  | User is on https://www.saucedemo.com/                                |
| Test Data     | Username: `standard_user` <br> Password: `secret_sauce`              |
| Steps         | 1. Enter valid username. <br> 2. Enter valid password. <br> 3. Click the Login button. |
| Expected      | User is redirected to the Products page and sees the product list.   |

---

## TC_UI_02 – Invalid Login (Wrong Password)

**Module:** Login  
**Priority:** High  

| Field         | Details                                                              |
|---------------|----------------------------------------------------------------------|
| Test Case ID  | TC_UI_02                                                             |
| Title         | Login fails with invalid password                                    |
| Precondition  | User is on https://www.saucedemo.com/                                |
| Test Data     | Username: `standard_user` <br> Password: `wrong_pass`                |
| Steps         | 1. Enter username. <br> 2. Enter wrong password. <br> 3. Click the Login button. |
| Expected      | Error message is shown and user stays on login page.                 |
