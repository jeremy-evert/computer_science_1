# Chaz Owner Note — Course Foundry Two-Commit Yellow

**Scope:** Independent Owner review for the CS1 Prompt 103/104 acceptance runway.  
**Production writes:** None.  
**Flo worktree touched:** No.

## Observation

At Flo startup, the shared Brandy `course_foundry` checkout was two commits ahead of `origin/main`. Flo deliberately created an isolated Course Foundry worktree from published `origin/main` rather than inheriting unexplained shared-checkout state.

The published baseline Flo selected was:

- `origin/main`: `a49b658f3a230ad74787757cb0ed66ba24d1c7e5`

Independent review of the Brandy session that created the two local commits identifies them exactly as follows.

## Local commit 1

- SHA: `4bd3dfd`
- Subject: `Complete Prompt 107's DSCT production course-id guard (was uncommitted)`
- Changed paths:
  - `course_foundry/dsct_desired_course.py`
  - `tests/test_dsct_desired_course.py`
- Recorded change size: 22 insertions, 2 deletions across those two files.
- Purpose: make DSCT production course-id guard behavior reproducible from Git after a prior DSCT session had used uncommitted working-tree state.

## Local commit 2

- SHA: `9ca412b`
- Subject: `Wire Week 3 container/LaTeX skill ladder into DSCT Canvas deployment`
- Changed paths:
  - `course_foundry/dsct_desired_course.py`
  - `tests/test_dsct_desired_course.py`
- Recorded change size: 56 insertions, 9 deletions across those two files.
- Purpose: wire already-authored DSCT Week 3 container/LaTeX material into the DSCT deployment plan.

The originating session explicitly recorded that only those two DSCT paths were staged for the second commit and that the remaining shared-checkout dirt belonged to an unrelated live CS1 experiment process and was left untouched.

## CS1 relevance determination

Neither ahead commit changes:

- `course_foundry/production_deploy.py`;
- CS1 desired-course/compiler code;
- CS1 Week 2 link-token resolution;
- CS1 grading/drop-rule behavior;
- Harbor file verification behavior;
- any CS1 Prompt 103/104 acceptance logic.

Therefore neither commit represents unpublished CS1 production truth required by Flo's 103/104 closeout.

The separate uncommitted `submission_listener` runtime/configuration state and Prompt 127 zero-submission experiment artifacts visible in the shared checkout are not these two commits. They remain protected shared-worktree state and are not authority for CS1 103/104 deployment.

## Owner conclusion

**YELLOW CLOSED — NOT CS1-RELEVANT.**

Flo was correct to exclude `4bd3dfd` and `9ca412b` by starting the bounded CS1 Course Foundry worktree from published `origin/main` at `a49b658f3a230ad74787757cb0ed66ba24d1c7e5`.

No interruption to Flo is required on this issue.
