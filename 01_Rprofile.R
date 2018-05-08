# I don't see a need to make any changes to .Rprofile if users decide to work on project
# in RStudio. Provided only for convention, is a condition to identify an RStudio Session

if (tail(strsplit(getwd(),"/")[[1]],1)=="polyreg_build") {
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/.Rprofile",
  '.Rprofile',quiet = TRUE)
}
invisible (file.show('.Rprofile'))

.rs.restartR()

# When you load a project using a <project>.Rproj file, the default behavior opens a 
# new project window and sets the working directory to the <project>.Rproj path.
# For this reason, I recommend keeping both .Rproj & .Rprofile in the VCS project root.
