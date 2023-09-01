# Zowe-Python-SDK: My Journey as a Summer Mentee

##### Written by Aaditya Sinha, Open Mainframe Project Summer 2023 Mentee

I am a 3rd year student at Noida Institute of Engineering and Technology, studying Computer Science and Engineering. I am an Open source enthusiast and the community of Open Mainframe Project looked interesting to me. I have been contributing to the Mainframe project for the past 1 and a half years.

## What is Zowe-Python-SDK 🚀:
Zowe is an integrated and extensible open-source framework for z/OS. Similar to popular operating systems like macOS and Windows, Zowe offers a core set of applications combined with APIs and OS capabilities. These components pave the way for future applications to be built upon. Zowe provides modern interfaces to interact with z/OS, allowing a cloud-platform-like experience. The Zowe-Python-SDK specifically enables the creation of client applications and scripts that interface with z/OS REST API interfaces. This SDK empowers Python developers to craft powerful applications for interacting with z/OS components.

## My role as Summer Mentee 🌞:
During my time as a Linux Foundation Mentee, I focused on enhancing the Zowe project. Specifically, I worked on finalizing team configuration support and other enhancements to facilitate a v2 release. This included adding support for Zowe v2 team configuration. I tackled various issues, such as:


## My acceptance into the program 🎉
“zowe-client-python-sdk” which was a set of Python packages designed to allow programmatic interactions with z/OS REST API interfaces with minimum effort.

It's 2022, I started contributing to it. 3–4 PRs of mine also got merged in the repo. I also talked with my mentor about the issues/PRs-related stuff. Then by the time I was contributing in the last week of May the deadline for the mentorship program was close. So I immediately submitted the requirements that were needed to apply resume, enrollment verification, and a cover letter containing answers to the questions asked. After a few weeks, I didn’t get any email from the organization and the mentorship program was about to start. Then I checked to mentorship page and saw that the mentees were already selected. I was shocked and disappointed of course.

I was too late to apply, they wanted to select mentees a week before I submitted
I was only lacking in experience as I was only in my second year, I didn’t have much experience or any projects in Python
This helped me so much, I continued contributing to the repository until the next year that 2023. I also got an internship in Python development in the meantime. Made some Python projects and some pretty good contributions.

Now, it's 2023. The time has come, I was working on a PR and did some meetings with Timothy. It was a pending PR though. My exams were starting so put them on hold. The applications were opened as Timothy said in one of our calls. Then I said, “Okay, I will apply this time”. I submitted my resume which was pretty good than the last time, enrollment identification, and cover letter.

I was pretty nervous. Every day I look at my Gmail. Then one day I was studying for my exam and suddenly a notification popped up. I opened it and saw the acceptance mail for the mentorship program. Yay!! Finally, my work paid off.

![](./acceptance.png)

## What did I do for 3 months? 💻
My main task was to enhance zowe-python-client-sdk for version 2 by adding features that were already in node.js SDK and adding z/OSMF Files and Jobs API.

For the first month, I was assigned some good first issues to add zos-files and zos-jobs API.

![](./issue1.png)

I learned a lot from these issues, how we can make use of utility methods, and how to create tests that can test more than one method.

After one and half months I was assigned to Zowe v2 Configuration which had the core features for the python-sdk.
I was working on 3 main issues with priority medium and high.

### 1. [core] Validate that zowe.config.json file matches schema #74

In this issue, we were given a `zowe.config.json` file that references a zowe.schema.json file. My task was to add a feature that would validate the contents of the JSON file to the schema file.

The main part was exception handling because there were different types of errors generated through the validation. Another difficult part was handling the `schema_property` which has to load from the internet URI.

However, the most time-consuming part was implementing unit tests. I learned a lot about unit testing while working on this issue. I also learned so much about the fake file system and how you can use different fake files for different tests.

### 2. Load profile properties from environment variables #136

When loading a profile team config, we can provide an `override_with_env` flag that will override the profile properties from the environment variables.

This was a really interesting task because I needed to work on the `env` variables. The most difficult task was to map these `env` variables to the profile properties which was also interesting simultaneously. I learned a lot about `env` variables and how can I add/use them in the tests.


### 3. Fix profile merge order to match Node.js SDK #190

Although I already worked on this issue before the mentorship, as I was also contributing to the zowe. It was easy for me to get my hands on it.

In this issue, the `ProfileManager.load` method was failing for the bas profile, it was not taking the `user` and the `password`. So, I just need to implement the logic that was already implemented in the NodeJs sdk to merge the layers and then perform

It was a great experience learning a lot about zowe-cli and how to work on complex projects. I also learned that unit tests are an important part of software engineering.

Last week I was able to complete all the tasks and make all the PRs ready to merge.

## Should you apply for the LFX Mentorship Programme too? 🤔
Are you interested in Open Source? Then, a Simple answer — Yes! Try applying for the program.

I am glad that I got this opportunity and have learned a lot during the span of 3 months. I think it’s a cool opportunity that you get mentored by amazing engineers who build tools to solve problems. Some perks of participating in the LFX Mentorship Programme include:

1. Learning: Being a newbie to the world of DevOps, I certainly have gained a lot of knowledge by exploring and working alongside people

2. Networking: This is one of the under-rated perks of any Open Source Programmes. Networking and interacting with the community improves one’s soft skills and promotes growth when you hear different views, opinions, and approaches to solving a problem.

3. Stipend: Who does not love a stipend while learning 😉, the LFX Mentorship Programme pays a great stipend, but I would advise participating in this program not for the stipend but for the above points.

Overall my journey has been a great experience and I would like to thank my mentors Timothy Johnson and Fernando Rijo Cedeno(such great mentors) for guiding me throughout the mentorship, I would like to thank the community that’s always active and helping for the betterment of such tools 😃.

This summarized my journey as a Linux Foundation’s Zowe Mentee and I hope this blog was informative.