<script>

// javascript implementation of the approach

// Function to return the binary
// equivalent of decimal value N
function decimalToBinary(N)
{

	// To store the binary number
	var B_Number = 0;
	var cnt = 0;
	while (N != 0)
	{
		var rem = N % 2;
		var c = Math.pow(10, cnt);
		B_Number += rem * c;
		N = parseInt(N/2);

		// Count used to store exponent value
		cnt++;
	}
	return B_Number;
}

// Driver code
var N = 17;
document.write(decimalToBinary(N));

</script>
