# # [Namespace Workflow](http://r-pkgs.had.co.nz/namespace.html#namespace-workflow) & [Code Workflow](http://r-pkgs.had.co.nz/r.html#r-workflow)

# Now we have to actually write some code. To make things easy, we'll copy
# existing code and save in our package R folder, [/home/cdsw/R/polyreg/R](../../rdev_build/files/R/polyreg/R/)

if (getwd()=="/home/cdsw") {
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/R/polyreg_r.R",
    paste0(getwd(),"/R/polyreg/R/polyreg_r.R"),quiet = TRUE)
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/R/polyreg_sparlyr.R",
    paste0(getwd(),"/R/polyreg/R/polyreg_sparklyr.R"),quiet = TRUE)
}

# If you inspect the code just loaded, you'll see that it has [roxygen comments](http://r-pkgs.had.co.nz/man.html#roxygen-comments).
con <- file("R/polyreg/R/polyreg_sparklyr.R","r")
cat(paste(readLines(con)[-(1:49)],collapse="\n")[1])
close(con)

# In addition, to creating our documentation for us (which we'll see later), [roxygen comments](http://r-pkgs.had.co.nz/man.html#roxygen-comments) also simplify defining our package [NAMESPACE](http://r-pkgs.had.co.nz/namespace.html#undefined).
# Check out our [NAMESPACE](../files/R/NAMESPACE) after running **devtools::document()**:
devtools::document("/home/cdsw/R/polyreg")
invisible(file.show('/home/cdsw/R/polyreg/NAMESPACE'))

# In general, the [Namespace Workflow](http://r-pkgs.had.co.nz/namespace.html#namespace-workflow) becomes:
#  * 1) Add roxygen comments to your [R](home/cdsw/R/polyreg/R) files.
#  * 2) Run **devtools::document(<PATH>)**
#  * 3) Review [NAMESPACE](../files/R/NAMESPACE) file and run checks/tests.
#  * 4) Rinse & Repeat until correct functions are imported/exported

# That's it, we can now load this package using dev tools and run a package function.
devtools::load_all("/home/cdsw/R/polyreg")
polyreg::plot_r()
polyreg::plot_sparklyr()

# In general, the [Code Workflow](http://r-pkgs.had.co.nz/r.html#r-workflow) becomes:
#  * 1) Edit an [R](home/cdsw/R/polyreg/R) file.
#  * 2) Run **devtools::load_all(<PATH>)**
#  * 3) Explore code in console.
#  * 4) Rinse & Repeat

# This workflow iteration is worth being familiar with. **load_all** roughly 
# simulated what happens when a package is installed and loaded with **library**
