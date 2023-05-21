import random, pyautogui, time

posts = ["Count me in!", "Anyone need a website?", "I'm with you!", "Starting my web design business!"]
commentCount = 0
clickTries = 0
pyautogui.FAILSAFE = False

def checkForPictureUploadButton():
    print('Looking for piture upload button')
    pictureUploadButton = pyautogui.locateOnScreen('logoButton.png')
    if pictureUploadButton == 'none': 
        print('No picture upload button found. Moving mouse')
        if clickTries >= 2: return
        clickTries += 1
        pyautogui.move(1216, 970)
        checkForPictureUploadButton()

    else:
        print('Picture upload button found')
        pyautogui.click(pictureUploadButton)
        time.sleep(2)
        pyautogui.write('logo.jpg')
        time.sleep(2)
        pyautogui.press('enter')

time.sleep(3)
while True:

    # Keep count of how many comments we've made. Take a break
    # at 10 so Facebook doesn't think we're a bot
    # print(commentCount)
    if commentCount >= 10:
        commentCount = 0
        time.sleep(30)
    
    # Choose a random comment to post
    comment = random.choice(posts)

    # Jump to the next post
    time.sleep(2)
    print('Finding next post')
    pyautogui.press('j')

    # Look for the comment button
    time.sleep(2)
    print('Looking for comment button')
    location = pyautogui.locateOnScreen('commentButton.png')

    # If we can't find the comment button, just move to the
    # next post. If we do find it, click it
    
    if location == None: 
        print(location)
        print('Comment button not found')
    else: 
        # Click comment button
        print('Clicking comment button')
        print(location)
        pyautogui.click(location)

        # Write the comment
        time.sleep(9)
        print('Writing comment')
        pyautogui.write(comment)

        # Click photo upload button and upload logo
        # checkForPictureUploadButton()

        # Post the comment
        time.sleep(2)
        print('Posting comment')
        pyautogui.press('enter')
        
        # Exit the comment section to start again
        time.sleep(2)
        print('Exiting comment section')
        pyautogui.moveTo(1074, 771)
        pyautogui.click()

        # Increase comment count by 1
        commentCount += 1