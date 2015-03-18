from flask import Flask, url_for, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #test dic to send to triton
        d = {
            'user_lang': 'en',
            'zones': [{
                'site_domain': u'www.loadtest.com',
                'zone_dsps': [{
                    'dsp_id': 1,
                    'dsp_api_version': u'v23',
                    'dsp_bid_url': u'http://stage-rtb.adsnative.com:5554/?v23=true',
                    'dsp_creative_id': 38865,
                    'dsp_uuid': 2056925886,
                    'user_buyeruid': '9XVyKW6WtxqszZV9x545c0f_jfU',
                    'dsp_advertiser_id': 566,
                    'dsp_campaign_id': 1004,
                    'dsp_floor_price': 2.5
                }],
                'zone_id': 280,
                'zone_price': 0.0,
                'zone_targets': [u'Uncategorized'],
                'zone_max_image_height': None,
                'network_id': 2,
                'zone_num_ads': 1,
                'site_id': 2,
                'zone_zone_id': u'rtb',
                'zone_admsupport_required': ['brandname'],
                'zone_ad_type': 0,
                'zone_max_image_width': None,
                'zone_max_title_length': 48,
                'zone_max_excerpt_length': 0,
                'zone_admsupport_optional': []
            }],
            'site_url': None,
            'user_ip': '192.168.42.1',
            'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36',
            'user_uuid': '83fc744b-8954-4103-8541-55446172c5ec'
        }

        url_in = request.form['url']
        useragent_in = request.form['useragent']
        userip_in = request.form['userip']
        buyeruid_in = request.form['buyeruid']

        #put in default values
        if not useragent_in:
            print 'there was no useragent!'
        if not userip_in:
            print 'there was no userip!'
        if not buyeruid_in:
            print 'there was no buyeruid!'

        d['site_url'] = url_in

        #creating json
        j = json.dumps(d)

        #sending post request
        url = 'http://triton.adsnative.com/rtb'
        header = {'Content-Type': 'application/json'}
        resp = requests.post(url, data=j, headers=header)
        r = resp.json()

        return render_template('response.html', d=r[0])

    return render_template('hello.html')

app.run()
