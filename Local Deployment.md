# Local Deployment

## Requirement
- nodejs 12.18.4
- docker
- Sebaiknya di linux atau windows/WSL2

## Codebase
- https://github.com/deedee/geonode branch: master
- https://github.com/deedee/geonode-mapstore-client branch: master
- https://github.com/deedee/MapStore2 branch:2022.01.xx-ddd

1. Clone & Push
Setelah di clone seraca local, lalu push ke repo pribadi di github

2. Edit Dependency
- geonode-mapstore-client/.gitmodule
```
url = https://github.com/<USERNAME>/MapStore2.git # ganti ke url private repo
branch = 2022.01.xx-ddd
```

- geonode/requirements.txt
```
-e git+https://github.com/<USERNAME>/geonode-mapstore-client.git@master#egg=django_geonode_mapstore_client # ganti ke url private repo
```

3. Deploy Mapstore2
- Setelah melakukan update, Push ke github
- cd ke `geonode-mapstore-client/geonode_mapstore_client/client`
- update submodule dan pastikan `geonode-mapstore-client/geonode_mapstore_client/client/Mapstore2` sudah berisi update yg sama dengan yg kita push barusan. Check git log nya.
- install deps & compile:
	npm i
	npm i git+https://github.com/geosolutions-it/react-draft-wysiwyg#v1.14.8
	npm i git+https://github.com/geosolutions-it/html-to-draftjs#v1.5.1
	npm run compile
- Setiap melakukan update Mapstore2 wajib menambahkan file baru yang berada di `geonode-mapstore-client/geonode_mapstore_client/client/static` hasil compile diatas ke repo, lalu commit
	cd <geonode-mapstore-client>
	git add geonode-mapstore-client/geonode_mapstore_client/client/static
	git commit -a

- Push `geonode-mapstore-client` ke github

4. Deploy Geonode
- cd <geonode>
- sh ./docker-build.sh

