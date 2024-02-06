__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

annotate_arg = snakemake.input.get("annotate", "")
annotate = ""
if annotate_arg:
    annotate = f"--annotate {annotate_arg}"

shell(
    "cnvkit.py target "
    "{snakemake.input.bed} "
    "-o {snakemake.output.bed} "
    "{annotate} "
    "{extra} "
    "{log}"
)
