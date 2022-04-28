def update_status_chargeoff(debug=True):
    import csv
    with open('update_status_chargeoff.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            for row in reader:
                try:
                    app = Application.objects.get(id=row['appid'])
                except:
                    print("app not found: {}".format(row['appid']))
                    continue
                print(app.id, app.status)
                if debug == False:
                    try:
                        app.status = Application.STATUS_CHARGEOFF
                        app.save()
                    except:
                        Application.objects.filter(id=row['appid']).update(status=Application.STATUS_CHARGEOFF)
        except Exception as e:
            print("exception: {}".format(str(e)))