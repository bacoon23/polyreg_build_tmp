# # [Vignette Workflow](http://kbroman.org/pkg_primer/pages/vignettes.html)
# Users don't always read documentation. Instead user intuition is to first
# seek out informative examples. Therefore we should write informative 
# examples that users can modify to thier interestes.

# R has a very good practice of having both vingette and demo conventions.
#
# **Demos** are longer, usually include user interaction, does not get tested
# during check processes, thus they can easily break without you knowing.
#
# **Vignettes** are shorter, include formatted input and output, are reexecuted
# during checks and are listed in CRAN package page.

# To build a template vingette in CDSW:
install.packages('rmarkdown',quiet=TRUE)
install.packages('pandoc', quiet=TRUE)
devtools::use_vignette("polyreg-vignette", pkg="/home/cdsw/R/polyreg")

# Again, this this creates a .gitignore file we don't need:
invisible(file.remove("/home/cdsw/R/polyreg/.gitignore"))

# To see an example build, we'll just build the provided template:
devtools::build_vignettes(pkg="/home/cdsw/R/polyreg")
system("ls -lR /home/cdsw/R/polyreg/inst/doc")

# NOTE: vignettes are not supported in CDSW. As example:
vignette('dplyr')

# Thus developing vignettes in CDSW awkward.
# We're also overlooking the fact that the vignette format is essentially
# the same as CDSW inline form.
# Optionally, title your CDSW script as 'demo' or 'vignette'


# So in general, **don't bother** with devtools::vignettes in CDSW.
# Instead, just use a CDSW script.
# If necessary for internal process or CRAN submission, dev in RStudio.

# Since we don't recommend vignettes in CDSW, let's clean up what we just did:
system("rm -rf /home/cdsw/R/polyreg/vignettes")
system("rm -rf /home/cdsw/R/polyreg/inst")
