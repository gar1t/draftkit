# Draft Kit

## Preparing the players list (manual)

These steps document the underlying process automated by
`dk-init`. Review these first and run `dk-init` (after optionally
editing the source weights that are hard-coded in that script) to
automate the steps.

### 1. Test each get-xxx script

Make sure each get-xxx script returns what you expect. Fix any
problems.

### 2. Create a working draft directory

The examples below (and those that follow) assume a working draft
directory named `draft-2017`. Modify as needed.

    $ mkdir draft-2017

### 3. Run get-all

    $ ./get-all draft-2017

This will generate csv files in the draft directory for each source.

### 4. Join sources

This step applies weights to each source file and generates a "joined"
file. To simplify the command we'll cd into the draft directory.

    $ cd draft-2017
    $ ../dk-join espn-ecr.csv:1 fantasypros-ecr.csv:1 ... > joined.csv

The joined file in this example is named joined.csv.

Note the warnings for players - if a player isn't found in any one of
the source files, his name is displayed with a warning. In most cases
these players will be low ranked and you don't need to worry.

To delete files that don't have enough sources, use the '-k /
--keep-source-min' option. For example, to keep players only when they
have at least 3 sources run:

    $ ../dk-join -k 3 ...

### 5. Apply a comparison source

To get an idea of the "value" picks, relative to a particular source,
use dk-apply. The source is almost always espn-ecr.csv, as this is the
source that the other players will be using for their draft.

    $ ../dk-apply joined.csv espn-ecr.csv > players.csv

This gives you a final players list.

## Automating preparation using dk-init

Edit `dk-init` to configure the sources and weights applied to each.

Run:

    $ ./dk-init DRAFT-DIR

where `DRAFT-DIR` is the name of the draft directory you'd like to
initialize.



## Using the players list

During a draft, use the following workflow.

### Start by listing all "value" players

    $ ../dk-value players.csv | less

The "+" values show the difference between your list and the
compared-to list (e.g. ESPN ECR - or whatever you think your opponents
will be using). Look for very large numbers. These are the players you
want to keep an eye out for as high value picks. In some cases you may
go down in the draft to get one of these players, or wait a pick or
two hoping your opponents don't have a bead on them.

Note that you will have the "+" (as well as "-") ranks during the
draft. This step is just to highlight the value players early on.

QBs are great value picks - look for one with a double digit value
score.

###
