|DRY|
#####

Programmers learn this mantra early in their education (or they should!)
Basically they are taught to factor out repeated code into a single function
that can be called whenever that code needs to be executed. That is certainly a
good way to reduce code bloat, and just makes sense.

But we repeat ourselves over and over in other ways without batting an eye!
Think about it:

How much duplication of effort is being spent on processing documentation files
using Sphinx_? How about recompiling source code files to build an application?

If you think about what is going on inside all of the basic tools we use on a
daily basis, you discover a lot of duplicate work. Eliminating that work should
be part of our goal to develop more efficient ways to get our work done.

DRY in |pylit| Development
**************************

In the |pylit| project, we will apply the |DRY| principle to the task of
managing documentation fragments contained in |LP| documents. This will be done
using a data store modeled after the one used by Git. Each fragment will be
extracted as a block, and a hash calculated for that block. This hash will be
used to store the fragment in the data store.

We will also store fragments of output text needed to produce the final documentation. For example, the HTML code needed to display the fragment will be generated once and saved. If the documentation changes, but the fragment remains unchanged, we will not need ot generate that HTML chunk again, saving processing time.

Obviously, this means we no longer rely n standard Sphinx_ processing, but
adding our own processing hooks is fairly easy to do, thanks to the modular
structure of the Sphinx_ code.

