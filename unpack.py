def total(galleons,sickles,knuts):
	return (galleons*17 + sickles)*29 + knuts

coins = {
	"galleons": 100,
	"sickles": 50,
	"knuts": 25
}
# unpack from coins
print(total(**coins),"knuts")

