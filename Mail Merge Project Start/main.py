from mail_merge import MailMerge

starting_letter = "/Users/andre/PycharmProjects/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters" \
                  "/starting_letter.txt"

name_list = "/Users/andre/PycharmProjects/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names" \
            "/invited_names.txt"

finished_letter = "/Users/andre/PycharmProjects/Mail+Merge+Project+Start/Mail Merge Project Start/Output/" \
                  "ReadyToSend"

place_holder = "[name]"

mail_merge = MailMerge(starting_letter, name_list, finished_letter, place_holder)
mail_merge.create_letters()


if __name__ == "main":
    pass
