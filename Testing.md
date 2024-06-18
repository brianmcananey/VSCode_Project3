# Testing <!-- omit in toc -->


## Automated vs Manual Testing

Automated testing and manual testing, when used in combination, are able to achieve a greater level of testing coverage. Automated testing is good for repetitive and critical tasks, while manual testing is good for new or changing requirements and exploratory testing.

---

<div align="center">

## Manual Testing

</div>

Manual testing allows the tester to explore the site and using experience and creativity to find any issues within the site. It also takes into account flexibility and context, manual testing paramaters can be changed quickly depending on the requirements. The tester can also take into account the prospective users and their knowledge of the system in order to execute tests that are relevant.  

| | Mobile S (320px)| Mobile L (425px)| Tablet (768px) | Desktop (1024px)|
|---|:---:|:---:|:---:|:---:|
|Responsive Images|✓|✓|✓|✓|
|Responsive Elements|✓|✓|✓|✓|
|Responsive Text|✓|✓|✓|✓|
|Responsive Nav Bar|✓|✓|✓|✓|

|Nav Bar Testing|Yes/No|
|---|:---:|
|Nav bar text and styles are loaded|✓|
|Nav bar collapse appears up to medium sized screens|✓|
|Nav links work as intended|✓|

|Index Page Testing|Yes/No|
|---|:---:|
|Hero image loads|✓|
|Reviews load|✓|
|Reviews are responsive when hovered over|✓|

|Sign Up Page Testing|Yes/No|
|---|:---:|
|Hero image loads|✓|
|Form Loads|✓|
|Form works|✓|

|Log In Up Page Testing|Yes/No|
|---|:---:|
|Hero image loads|✓|
|Form Loads|✓|
|Form works|✓|

|Contact Page Testing|Yes/No|
|---|:---:|
|Hero image loads|✓|
|Form Loads|✓|
|Form works|✓|

|Log out Function Testing|Yes/No|
|---|:---:|
|Hero image loads|✓|
|Form Loads|✓|
|Form works|✓|
|Log Out appears in navbar|✓|
|Logout function works|✓|


<div align="center">

## Automated Testing

</div>

Automated tests are repeatable and reliable as there is limited risk for human error. It allows for testing on both a small and a large scale in a quick and efficient manner. Automated testing might be used to test the performance of a site in order to ensure that it can handle page loading.

# Responsiveness

Responsivity tests were carried out using Google Chrome DevTools. Device screen sizes covered include:

- iPhone SE
- iPhone 12 Pro
- Samsung Galaxy S20 Ultra
- iPad Air
- Surface Pro 7
- Surface Duo
- Samsung Galaxy A51/71

I also personally tested the website on Samsung Galaxy S22, Samsung Chrome book, Dell XPS 15 laptop and a Dell widescreen monitor.

### Lighthouse <!-- omit in toc -->

| Page | Test Results | Lighthouse Suggested Improvements |
|:---:|---|---|
|Index|![Index Lighthouse testing](static/images/hompage-lighthouse.png)|Specifying a specific width and height of my title image, I wanted to retain as much responsivity as I could and opted to use bootstrap instead.|
|About Page|![About Page Lighthouse testing](static/images/aboutpage-lighthouse.png)|Properly sizing the images would reduce load time and cellular data, currently some images are oversized and are slowing down the time it takes for the page to load.|
|Sign Up|![Sign Up Lighthouse testing](static/images/signup-lighthouse.png)|Similar results to the Index page, page is loading well.|
|Log In|![Log In Lighthouse testing](static/images/login-lighthouse.png)|Similar results to the Index page and Sign up page, page is loading well.|
|Contact|![Contact Page Lighthouse testing](static/images/contact-lighthouse.png)|Similar results to the Index page and Sign up page, page is loading well.|
|Mobile|![Mobile Lighthouse testing](static/images/mobile-lighthouse.png)|The didnt perform as well as the desktop testing, need to review image sizes and loading times to improve the performance.|


### HTML and CSS Validation <!-- omit in toc -->

### HTML <!-- omit in toc -->

![HTML Validation]()

- All of the HTML pages passed the W3C HTML Validator.

### CSS <!-- omit in toc -->

![CSS Validation](static/images/css-validation.png)

- All pages passed the W3C CSS Validation.

# A11y Color Contrast Accessibility Checker

All website pages were tested using the A11y Color Contrast Accessibility Checker and no automated colour contrast issues were found.

![a11y Color Validation](static/images/a11y-validator.png)

## JavaScript Testing <!-- omit in toc -->

- Throughout development I used console logs to test that the functions worked as intended.

## Python Testing <!-- omit in toc -->

- Throughout I tested in the terminal.

![Python Terminal](static/images/terminal-debug.png)

- 


# Peer Review

I asked a number of friends both inside and outside of the Code Institute community for feedback on my project. The feedback on the website and documentation was positive.

It was suggested that I could add additional features to the site, which included links to each restaurant and to edit the styling of the log out navbar.


## Known bugs and fixes

- Styling of the Navbar when logged in isn't as good as it should be, need to improve the css for "logout"
- The performance level of the About page needs improving to speed up loading time. This can be fixed at a later date as I did not have time.
- Add extra security in the form of a confirm password on the sign up page.