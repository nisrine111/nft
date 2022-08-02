from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_account, OPENSEA_URL

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def set_token_uri():
    print(f"currently working on{network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f" you have created {number_of_advanced_collectibles} collectibles")
    for token_id in range(number_of_advanced_collectibles):
        breed = advanced_collectible.tokenIdToBreed(token_id)
        if not advanced_collectible.tokenURI(token_id).startsWith("https://"):
            print(f"setting token URI {token_id}")
            set_tokenURI(advanced_collectible, token_id, dog_metadata_dic[breed])


def set_tokenURI(nft_contract, token_id, token_uri):
    tx = nft_contract.setTokenURI(token_id, token_uri, {"from": get_account()})
    tx.wait(1)
    print(
        f" now you can see your NFT on {OPENSEA_URL.format(nft_contract.address,token_id)}"
    )
    print("wait a bit then press the refresh metadata button")
