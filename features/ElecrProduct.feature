Feature: Electronics product
  Scenario Outline: Verify section in Electronics product
    Given we navigate to Flipkart url
    Then we type in the "<number>" edit box
    And we type in the "<password>" field
    And we click on the login button
    Then type "<search>" in searchbox
    And click on search button
    Then click on product name
    Then switch to new window
    Then check diffrent images of the product
    And Give "<pincode>"
    And click on check
    Then click on wishlist
    Then click on read more in specifactions


    Examples:
      | number | password | search | pincode |
    | 6266739954 | Rudresh@123 | Mobile | 450001 |
    | 6266739954 | Rudresh@123 | TV | 450001 |
    | 6266739954 | Rudresh@123 | Laptop | 450001 |
