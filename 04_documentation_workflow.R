# Help in RStudio shows up in the viewer, not in console
?devtools::document

# Otherwise, it works the exact same
devtools::load_all("R/polyreg")
help(polyreg::gen_dat_r)