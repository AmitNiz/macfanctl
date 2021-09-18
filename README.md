# macfanctl
Simple macbook fan control tool for linux.


#### TODOs:
* add deamon mode with various profiles for automatic fans control.

#### Quick Installation:
| Method    | Command                                                                                           |
|:----------|:--------------------------------------------------------------------------------------------------|
| **wget**  | `sh -c "$(wget -O- https://raw.githubusercontent.com/AmitNiz/macfanctl/main/install.sh)"`   |
| **curl**  | `sh -c "$(curl -fsSL https://raw.githubusercontent.com/AmitNiz/macfanctl/main/install.sh)"` |
| **fetch** | `sh -c "$(fetch -o - https://raw.githubusercontent.com/AmitNiz/macfanctl/main/install.sh)"` |




## cli Mode:

      usage: macfanctl.py [-h] [-i {value}] [-d {value}] [-s {value}] [-g]

      optional arguments:
        -h, --help            show this help message and exit
        -i {value}, --inc {value}
                              increases the fan's speed by a given value in the range [0 - {max_value}].
        -d {value}, --dec {value}
                             decreases the fan's speed by a given value in the range [0 - {max_value}].
        -s {value}, --set {value}
                             sets the fans speed to a given value in the range [0 - {max_value}].
        -g, --get             prints the fan's speed.
        


`*Tested On mbp 2015.`
