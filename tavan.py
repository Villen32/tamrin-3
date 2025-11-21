adad = int(input("yek adad do raghami vared kon: "))

yekan = adad % 10
dahgan = adad // 10

aval_be_tavan_dovom = dahgan ** yekan
dovom_be_tavan_aval = yekan ** dahgan

print("raghame aval be tavane dovom:", aval_be_tavan_dovom)
print("raghame dovom be tavane aval:", dovom_be_tavan_aval)
