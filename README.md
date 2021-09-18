# macfanctl
Fan control tool for linux machines on macbooks.


### TODOs:
* add deamon mode with various profiles for automatic fans control.

## cli Mode:

      usage: macfanctl.py [-h] [-i {value}] [-d {value}] [-s {value}] [-g]

      optional arguments:
        -h, --help            show this help message and exit
        -i {value}, --inc {value}
                              increases the fan's speed by a given value in the range [0 - 6199].
        -d {value}, --dec {value}
                             decreases the fan's speed by a given value in the range [0 - 6199].
        -s {value}, --set {value}
                             sets the fans speed to a given value in the range [0 - 6199].
        -g, --get             prints the fan's speed.
        


`*Tested On mbp 2015.`
