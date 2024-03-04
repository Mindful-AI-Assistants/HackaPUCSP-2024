
# Contributing

## Security / Disclosure

If you find any bug with HACKAPUC-SP code that may be a security problem, then contact at: [MindfulAI Copilots & Bots](https://github.com/MindfulAI-Copilots-Bots).
This way we can evaluate the bug and hopefully fix it before it gets abused.
Please give us enough time to investigate the bug before you report it anywhere else.

Please do not create GitHub issues for security-related doubts or problems.

## Support

If you want help with your Renovate configuration, go to the discussions tab in the Renovate repository and open a new "config help" discussion post.

## Bug Reports and Feature Requests

**Bugs**: First search for related bugs in the issues and discussions, if you don't find anything then:

1. Create a minimal reproduction
1. Open a new _discussion_ and link to the minimal reproduction

For **feature requests**: first search for related requests in the issues and discussions, if you don't find anything: create a _discussion_.

## Rate Limiting of Support Requests through Temporary Blocking

To ensure that the Renovate maintainers don't burn out from dealing with unfriendly behavior, those who display a bad attitude when asking for or receiving support in the repo will be rate limited from further requests through the use of temporary blocking.
The duration of the temporary block depends on how rude or inconsiderate the behavior is perceived to be, and can be from 1-30 days.

If you have been blocked temporarily and believe that it is due to a misunderstanding, or you regret your comments and wish to make amends, please reach out to the lead maintainer Rhys Arkins by email with any request for early unblocking.
If/once you are unblocked, you should edit or delete whatever comment lead to the blocking, even if you did not intend it to be rude or inconsiderate.
Long emails or apologies are undesirable - the maintainers are busy and want to be able to help as many users as possible with the time they have available.

## Code

If you would like to fix a bug or work on a feature, please fork the repository and create a Pull Request.
To learn how to setup your local workstation correctly read docs/development/local-development.md.
Also skim the docs/development folder, it has a lot of helpful information on things like adding a new package manager, how Renovate branches work, design decisions and more.

Before you start any Pull Request, it's recommended that you open a discussion first if you have any doubts about requirements or implementation.
That way you can be sure that the maintainer(s) agree on what to change and how, and you can hopefully get a quick merge afterwards.
Also, let the maintainers know that you plan to work on a particular issue so that no one else starts any duplicate work.

### Tests

Pull Requests can only be merged once all status checks are green, which means `pnpm test` passes, and coverage is 100%.

Use these commands to help run your tests:

- To run a single test folder, specify the path

  ```bash
  pnpm jest platform/gitlab

- To run against a single test file, specify down to the filename (suffix is not necessary)

   ```bash
   pnpm jest platform/gitlab/index



#### <p align="center"> 🌎💙 **One People. One World. One Spirit...We Are All One!** </p>



