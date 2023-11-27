Feature: Login to the application and create two rooms
  Scenario: Logging in with admin/password
    Given I open the login page
    When I log in with username "admin" and password "password"
    And I create room with number "102" and price "100"
    And I create room with number "103" and price "150"
    Then I should be logged in successfully
    And I should see "102-$100" and "103-150$" listed in the rooms

  Scenario: Check API Status and ID Field
    Given the API is accessible
    When I check the API status
    Then the API status should be 200
    And the field completed for ID 5 should be false

