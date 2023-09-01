# getHealth
Take home test assignment for SRE

Program prompts user to input a file path to a yaml config file using formatting from the assignment example
Once file is validated and imported it will begin checking all endpoints every 15 seconds to determine if UP or DOWN based on assignment criteria (response code 200 - 299 and less than 500ms response time)
After user cancels the program with ctrl + c it will calculate the total UP percentage per domain and print text for the UP percentage per domain

Example yaml file is included
