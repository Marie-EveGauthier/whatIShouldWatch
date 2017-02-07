<?php

namespace Tuto\TestBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller {

    public function testAction() {
        $film = $this->getDoctrine()
                ->getRepository('TutoTestBundle:films')
                ->findall();

        return $this->render('TutoTestBundle:Default:filmview.html.twig', array(
                    'film' => $film));
    }

    public function filtersAction() {

        return $this->render('TutoTestBundle:Default:filters.html.twig');
    }

    public function resultatAction() {
// for the request DBL
        $em = $this->getDoctrine()->getManager();
        // to get the value of the checkbox
        $checked_woman = $this->get('request')->request->get('dialogueWomen');
        $checked_bechdel = $this->get('request')->request->get('bechdel');
        if (($checked_woman) && ($checked_bechdel)) {
            $query = $em->createQuery(
                    'SELECT p
    FROM TutoTestBundle:films p
    WHERE p.dialogueWomen > p.dialogueMen and p.bechdel>0 ORDER BY p.title'
            );

            $products = $query->getResult();
            return $this->render('TutoTestBundle:Default:resultat.html.twig', array(
                        'products' => $products));
        } else if ($checked_woman) {
            $query = $em->createQuery(
                    'SELECT p
    FROM TutoTestBundle:films p
    WHERE p.dialogueWomen > p.dialogueMen ORDER BY p.title'
            );

            $products = $query->getResult();
            return $this->render('TutoTestBundle:Default:resultat.html.twig', array(
                        'products' => $products));
        } else if ($checked_bechdel) {
            $query = $em->createQuery(
                    'SELECT p
    FROM TutoTestBundle:films p
    WHERE p.bechdel > 0 ORDER BY p.title'
            );

            $products = $query->getResult();
            return $this->render('TutoTestBundle:Default:resultat.html.twig', array(
                        'products' => $products));
// If there is no movie that match the search
        } else {
            return $this->render('TutoTestBundle:Default:noResult.html.twig')
            ;
        }
    }

    public function aboutAction() {

        return $this->render('TutoTestBundle:Default:about.html.twig');
    }

}
