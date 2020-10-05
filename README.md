# Dumb_calculator
An independent, didactic project to learn the basics of Selenium. Instead of using you default calculator, this bot opens a Chrome tab, searches for their calculator and types in the operation you asked in the python terminal.

Current google-chrome version is 85.0.4183. Some issues had occurred regarding unmatching versions, solved with ChromeDriverManager().install(). More problems may arise, since any changes in the xpaths or the overall structure of Google main html page leave this bot helpless.

The process of this code is the following:
 - gocalc: Opens a Google tab. Closes the cookies pop-up frame, types 'calculator' in the search bar, closes the recent searches frame and clicks on Search.
 - defnum / defop: Stores the xpaths of every number in the Google calculator, as well as the operators '+', '-' and '=' in lists. (This bot can only calculate sums and       substractions, thus its name).
 - traduct: It matches every single character in the input operation (strings) with the corresponding operation/number in defop/defnum, and click on them.
 
 After this process, the user gets a very inefficient but sometimes accurate result for their extremely simple question.
