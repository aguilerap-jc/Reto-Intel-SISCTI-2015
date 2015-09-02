import facebook

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "642153615917075",  # Step 1
    "access_token" : "CAAL5CfdWRIEBAHodHWlY78Ldq8QoYC5wEYDtZC2oOinzFQMqmZAgKk4hZAcJXivA0oR5mrIfZCD5rcbBdofZBGl0Mjv7d0ZAcJ6ZAL83ZCrmPk155B5Xv66JcfSG5jxHTCfOLF36PE6e0VMWmZBZCA4OK48e91ByKCdHLZCeJ53vSRaLQT9wxST3wVIq2O97jCkX98QlfsDoelS8VCtCl5F87b9"   # Step 3
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main()
