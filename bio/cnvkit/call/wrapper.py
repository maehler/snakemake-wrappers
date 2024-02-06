__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

vcf = ""
vcf_arg = snakemake.input.get("vcf")
if vcf_arg:
    vcf = f"-v {vcf_arg}"

purity = ""
purity_arg = snakemake.params.get("purity")
if purity_arg:
    purity = f"--purity {purity_arg}"

ploidy = ""
ploidy_arg = snakemake.params.get("ploidy")
if ploidy_arg:
    ploidy = f"--ploidy {ploidy_arg}"

filter = ""
filter_arg = snakemake.params.get("filter")
if filter_arg:
    filter = f"--filter {filter_arg}"

extra = snakemake.params.get("extra", "")

shell(
    "(cnvkit.py call {snakemake.input.segment} "
    "{vcf} "
    "-o {snakemake.output.segment} "
    "{purity} "
    "{ploidy} "
    "{filter} "
    "{extra}) "
    "{log}"
)
