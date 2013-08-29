from app import App


def main():
    '''(NoneType) -> int
    Reads initializing data from init.txt and barchart data for a single
    barchart to load from input.txt. If either of these initializations fail,
    the program exits. Otherwise, the barchart is loaded. The user can then
    only quit the program.

    The script will attempt to scale the barchart data appropriately to fit
    whatever window size, but this is limited.
    
    This is a rough script with generally rough results, intended only as a
    learning exercise.'''
    return App().main()

if __name__ == "__main__":
    print(main()) # DEBUG ####################################################
