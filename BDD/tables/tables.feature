

Feature: As a writer for Acme
	I This is very serious stuff.

	Given a set of specific users:

	 | name      | department   |
	 | Barry     | Beer Cans    |
	 | Pudey     | Silly Walks  |
	 | Two-Lumps | Silly Walks  |

	When we count the number of people in the department
	Then we will find two people in "Silly Walks"
	 But we find one person in "Beer Cans"
	 	 	 

