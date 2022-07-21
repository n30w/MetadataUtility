import finder
import xh

x = xh.ExcelHandler()
f = finder.FindMeOccurrences()

if __name__ == '__main__':
    p = finder.FindMeFilePaths().get_paths()
    z = finder.FindMeVideo()

    # Words to search for in YouTube videos
    search_words = [
        "Library",
        "Librarian",
        "Book",
        "Books",
        "Learning",
        "Commons",
        "Reading",
        "Campus",
        "Cooke"
    ]

    # Export entire channel to Excel document
    # x.export_found_to_file(
    #     finder.FindMeVideo().full_vid_list("PUTURLHERE"),
    #     p["Desktop"] + "xh.xlsx"
    # )

    # Export timecodes from links.txt
    x.export_timecode_to_file((p["Desktop"] + "timecodes.xlsx"), True)

    # x.export_found_to_file(
    #     z.names(
    #         "Channel Name",
    #         search_words
    #     ),
    #     p["Desktop"] + "found.xlsx"
    # )

    # x.export_printer_to_file(p["Desktop"] + "prints.xlsx")

    # Export collection of selected DV names to Excel file
    # find = "Variety Show"
    # x.export_collected_to_file(p["Desktop"] + f"{find}.xlsx", find)
