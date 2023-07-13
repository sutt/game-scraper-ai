
## Can code interpreter find info from sites?

 - [x] Find url to store's site from the forum post:
    - input: https://boardgamegeek.com/guild/2570
    - output: https://chat.openai.com/share/32c74dd1-f983-4b7a-a1fb-5ccaccd7da81


 - [x] Find [best] email address from the site:
    - input: https://boardsandbrewsnh.com/
    - output https://chat.openai.com/share/11a59b56-cb16-4973-8764-0c840456d65e


## ChatHTML2Markdown converter

 - want to be able to link to particular section in chat from another readme

  - checklist of parser features to have:
    - [ ] handles code formatting
    - [ ] handles links
    - [ ] handles markdown in responses
    - [ ] particular sections are linkable via slugs

 - Random questions:
    - individual text span highlightingin markdown?

 - Resources:
    - https://www.markdownguide.org/extended-syntax/


# General Information

 - API structure:
    - https://boardgamegeek.com/guild/4049
    - https://boardgamegeek.com/user/steve122
    - https://boardgamegeek.com/boardgame/521/crokinole
        - /ratings?status=own : get list of all owners of this game

 - Notes:
   - A guild might have a manager listed which will point to a user
   - But users can't be messaged without an account, called "geekmail"



# Random Thoughts:

 - Extracting all text from the html and putting it into a markdown type format might be best for: 
    - helping model reason about it
    - keeping the number of tokens economical
 
 - Create vscode snippets for common syntax in markdown notes

 - How do you log react/client side rendering sites? Selenium?

 - How to make a 