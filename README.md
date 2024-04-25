# RUVerify
Our HackRU Spring 23 Project

A camera-based verification system that could be used in certain facilities in Rutgers University- New Brunswick instead of scanning your cards to enter those certain facilities.

For example, let's say you forgot your Rutgers ID and you want to enter the gym, but you need your id to enter the gym. What do you do in this case?
  - Fortunately, this face recognition system can prevent cases like this from happening.

How this is implemented:
  - We need a sign in page for Rutgers students to register for an account implemented using Flet, a Python framework used to create Flutter applications. 
      - Enter your NetID and sign in. Once you sign in, you now have an account.
 - Instead of scanning/signing in all of the time, now that you as a Rutgers student have an account, staff at facilities can use this verification system to
 take a picture of you signing in.
   - This verification system later then uses face recognition similarity algorithms implemented in the OpenCV module to recognize and verify you entering
 in the facilities.
 
 Overall, this verification system can make people's lives easier and saves time, and provides an alternative to verifying people physically.
