from brownie import FundMe, network, MockV3Aggregator, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT



def deploy_fund_me():
    account = get_account()
    # pass the price feed adress to our fundme contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address =config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        

    fund_me = FundMe.deploy(price_feed_address,
                            {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify"),
                            )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()

